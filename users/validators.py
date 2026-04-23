from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from .models import PasswordHistory

class PasswordHistoryValidator:
    """
    Валідатор, який перевіряє, чи не використовував користувач цей пароль раніше.
    """
    def validate(self, password, user=None):
        if user is None or not user.pk:
            return

        # 1. Перевірка: чи не співпадає з ПОТОЧНИМ паролем
        if check_password(password, user.password):
            raise ValidationError(
                "Новий пароль не може співпадати з поточним.",
                code='password_reuse',
            )

        # 2. Перевірка: чи не співпадає зі СТАРИМИ паролями з історії
        history = PasswordHistory.objects.filter(user=user)
        for past_pass in history:
            # check_password безпечно порівнює введений текст із зашифрованим хешем
            if check_password(password, past_pass.password_hash):
                raise ValidationError(
                    "Ви вже використовували цей пароль раніше. Придумайте новий.",
                    code='password_reuse',
                )

    def get_help_text(self):
        return "Пароль не повинен співпадати з вашими попередніми паролями."