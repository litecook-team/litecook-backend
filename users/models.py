from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.dispatch import receiver
from allauth.account.signals import email_confirmed
from allauth.socialaccount.signals import social_account_added
from django.db.models.signals import post_save, pre_save, post_delete
from allauth.account.models import EmailAddress
from django.contrib.postgres.fields import ArrayField

from django.utils import timezone
from datetime import timedelta

# Ваші імпорти з інших додатків
from recipes.models.recipe import Recipe, Diet, Cuisine, UnitChoice
from recipes.models.ingredient import Ingredient

from allauth.account.signals import user_signed_up


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

    is_banned = models.BooleanField(default=False, verbose_name="Заблокований")
    banned_until = models.DateTimeField(null=True, blank=True, verbose_name="Заблокований до")
    ban_reason = models.TextField(blank=True, null=True, verbose_name="Причина блокування")
    last_activity = models.DateTimeField(null=True, blank=True, verbose_name="Остання активність")

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

    def is_online(self):
        """Перевіряє, чи був користувач активний останні 5 хвилин"""
        if self.last_activity:
            now = timezone.now()
            return now - self.last_activity < timedelta(minutes=5)
        return False

    is_online.boolean = True
    is_online.short_description = "Онлайн"

    USERNAME_FIELD = 'email'
    # Вказуємо, що при створенні адміна через консоль, система має запитати Ім'я
    REQUIRED_FIELDS = ['first_name']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} ({self.email})"


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


# =======================================================
# МОДЕЛЬ ДЛЯ ВІДСТЕЖЕННЯ СЕСІЙ
# =======================================================
class UserActivityLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='activity_logs')
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="IP адреса")

    # Сучасні розпарсені дані
    os = models.CharField(max_length=50, blank=True, null=True, verbose_name="Операційна система")
    browser = models.CharField(max_length=50, blank=True, null=True, verbose_name="Браузер")
    device_type = models.CharField(max_length=50, blank=True, null=True, verbose_name="Тип пристрою")

    country = models.CharField(max_length=100, blank=True, null=True, verbose_name="Країна")
    last_endpoint = models.CharField(max_length=255, blank=True, null=True, verbose_name="Остання дія (URL)")

    first_seen = models.DateTimeField(auto_now_add=True, verbose_name="Перший вхід")
    last_seen = models.DateTimeField(auto_now=True, verbose_name="Остання активність тут")
    is_active_session = models.BooleanField(default=True, verbose_name="Токен активний")

    class Meta:
        verbose_name = "Сесія користувача"
        verbose_name_plural = "Сесії користувачів"
        ordering = ['-last_seen']

    def __str__(self):
        return f"{self.user.email} - {self.os} ({self.browser})"


# =======================================================
# СИГНАЛИ (АВТОМАТИЗАЦІЯ)
# =======================================================

@receiver(email_confirmed)
def update_user_email_verified(request, email_address, **kwargs):
    user = email_address.user
    user.is_email_verified = True
    user.save(update_fields=['is_email_verified'])


# 1. Спрацьовує при ПЕРШІЙ РЕЄСТРАЦІЇ через Google/Facebook
@receiver(user_signed_up)
def auto_verify_new_social_login(request, user, **kwargs):
    # Якщо в kwargs є 'sociallogin', значить це вхід через соцмережу
    if 'sociallogin' in kwargs:
        user.is_email_verified = True
        user.save(update_fields=['is_email_verified'])

        EmailAddress.objects.get_or_create(
            user=user,
            email=user.email,
            defaults={'verified': True, 'primary': True}
        )


# 2. Спрацьовує, якщо існуючий юзер просто прив'язує соцмережу
@receiver(social_account_added)
def auto_verify_linked_social_login(request, sociallogin, **kwargs):
    user = sociallogin.user
    if not user.is_email_verified:
        user.is_email_verified = True
        user.save(update_fields=['is_email_verified'])

    if user.email:
        EmailAddress.objects.get_or_create(
            user=user,
            email=user.email,
            defaults={'verified': True, 'primary': True}
        )

@receiver(post_save, sender=CustomUser)
def auto_verify_superuser(sender, instance, created, **kwargs):
    if instance.is_superuser:
        EmailAddress.objects.get_or_create(
            user=instance,
            email=instance.email,
            defaults={'verified': True, 'primary': True}
        )
        if not instance.is_email_verified:
            instance.is_email_verified = True
            instance.save(update_fields=['is_email_verified'])

# === Сигнали для ФІЗИЧНОГО ВИДАЛЕННЯ ФАЙЛІВ (Аватар, Рецепти, Інгредієнти) ===

@receiver(pre_save, sender=CustomUser)
def delete_old_avatar_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        old_user = CustomUser.objects.get(pk=instance.pk)
    except CustomUser.DoesNotExist:
        return
    if old_user.avatar:
        if not instance.avatar or old_user.avatar != instance.avatar:
            old_user.avatar.delete(save=False)


@receiver(post_delete, sender=Recipe)
def delete_recipe_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)


@receiver(pre_save, sender=Recipe)
def delete_old_recipe_image_on_update(sender, instance, **kwargs):
    if not instance.pk: 
        return
    try:
        old_obj = Recipe.objects.get(pk=instance.pk)
    except Recipe.DoesNotExist:
        return
    if old_obj.image and (not instance.image or old_obj.image != instance.image):
        old_obj.image.delete(save=False)


@receiver(post_delete, sender=Ingredient)
def delete_ingredient_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)


@receiver(pre_save, sender=Ingredient)
def delete_old_ingredient_image_on_update(sender, instance, **kwargs):
    if not instance.pk: 
        return
    try:
        old_obj = Ingredient.objects.get(pk=instance.pk)
    except Ingredient.DoesNotExist:
        return
    if old_obj.image and (not instance.image or old_obj.image != instance.image):
        old_obj.image.delete(save=False)