from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings


class CustomAccountAdapter(DefaultAccountAdapter):

    # 1. Посилання для підтвердження пошти при реєстрації
    def get_email_confirmation_url(self, request, emailconfirmation):
        # Використовуємо змінну з settings.py
        return f"{settings.FRONTEND_URL}/confirm-email/{emailconfirmation.key}"

    # 2. Посилання, яке прийде в листі для "Забули пароль?"
    def get_reset_password_from_key_url(self, reset_password_key):
        return f"{settings.FRONTEND_URL}/reset-password-confirm/{reset_password_key}"