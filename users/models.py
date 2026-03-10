from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.dispatch import receiver
from allauth.account.signals import email_confirmed
from django.db.models.signals import post_save
from allauth.account.models import EmailAddress


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

    # Робимо email головним полем для авторизації
    email = models.EmailField(unique=True, verbose_name='Email')

    # використовуємо стандартне поле для "Ім'я" з макетів і робимо його обов'язковим
    first_name = models.CharField(max_length=150, verbose_name='Ім\'я')

    # Поле згідно з ТЗ
    dietary_preferences = models.CharField(max_length=255, blank=True, null=True, verbose_name="Дієтичні обмеження")
    # Прапорець для перевірки, чи підтвердив юзер пошту
    is_email_verified = models.BooleanField(default=False, verbose_name="Email підтверджено")

    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Аватар')
    allergies = models.CharField(max_length=255, blank=True, null=True, verbose_name="Алергії (через кому)")
    favorite_cuisines = models.CharField(max_length=255, blank=True, null=True, verbose_name="Улюблені кухні")

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