from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.dispatch import receiver
from allauth.account.signals import email_confirmed
from django.db.models.signals import post_save
from allauth.account.models import EmailAddress
from django.contrib.postgres.fields import ArrayField

from recipes.models.recipe import Diet, Cuisine, UnitChoice

class CustomUserManager(BaseUserManager):
    """Кастомний менеджер для створення користувачів за email"""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email є обов\'язковим полем')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    # Видаляємо логін, бо він нам не потрібен
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=150, verbose_name='Ім\'я')

    # Прапорець для перевірки, чи підтвердив юзер пошту
    is_email_verified = models.BooleanField(default=False, verbose_name="Email підтверджено")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Аватар')
    allergies = models.ManyToManyField('recipes.Ingredient', blank=True, verbose_name="Алергії на інгредієнти")

    dietary_preferences = ArrayField(
        models.CharField(max_length=30, choices=Diet.choices),
        blank=True, null=True,
        verbose_name="Дієтичні обмеження"
    )
    favorite_cuisines = ArrayField(
        models.CharField(max_length=50, choices=Cuisine.choices),
        blank=True, null=True,
        verbose_name="Улюблені кухні"
    )

    USERNAME_FIELD = 'email'
    # Вказуємо, що при створенні адміна через консоль, система має запитати Ім'я
    REQUIRED_FIELDS = ['first_name']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} ({self.email})"

@receiver(email_confirmed)
def update_user_email_verified(request, email_address, **kwargs):
    user = email_address.user
    user.is_email_verified = True
    user.save()


@receiver(post_save, sender=CustomUser)
def auto_verify_superuser(sender, instance, created, **kwargs):
    """
    Якщо користувач створюється через консоль як Суперадмін,
    ми автоматично створюємо йому підтверджену адресу в allauth,
    щоб він міг одразу залогінитись через React.
    """
    if instance.is_superuser:
        # Створюємо або отримуємо запис EmailAddress для allauth
        EmailAddress.objects.get_or_create(
            user=instance,
            email=instance.email,
            defaults={'verified': True, 'primary': True}
        )
        # Також ставимо нашу зелену галочку в CustomUser
        if not instance.is_email_verified:
            instance.is_email_verified = True
            instance.save(update_fields=['is_email_verified'])


class UserIngredient(models.Model):
    """Модель для зберігання інгредієнтів, які є у користувача вдома (Інвентар/Холодильник)"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='inventory', verbose_name="Користувач")
    ingredient = models.ForeignKey('recipes.Ingredient', on_delete=models.CASCADE, verbose_name="Інгредієнт")

    amount = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Кількість")
    unit = models.CharField(max_length=20, choices=UnitChoice.choices, default=UnitChoice.G,
                            verbose_name="Одиниця виміру")

    # ================= Метадані часу =================
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Додано у холодильник")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Останнє оновлення кількості")

    class Meta:
        verbose_name = "Мій інгредієнт"
        verbose_name_plural = "Інвентар користувачів"
        unique_together = ('user', 'ingredient')
        # продукти, кількість яких юзер оновив найсвіжіше, будуть зверху
        ordering = ['-updated_at']

    def __str__(self):
        if self.amount is not None:
            clean_amount = self.amount.normalize()
            return f"{self.ingredient.name} - {clean_amount} {self.get_unit_display()}"
        return f"{self.ingredient.name} - {self.get_unit_display()}"