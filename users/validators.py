from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from django.utils.translation import get_language
from .models import PasswordHistory

def t_val(key):
    lang = get_language() or 'uk'
    lang = lang[:2]
    msgs = {
        'same_as_current': {
            'uk': "Новий пароль не може співпадати з поточним.",
            'en': "The new password cannot be the same as the current one.",
            'pl': "Nowe hasło nie może być takie samo jak obecne."
        },
        'used_before': {
            'uk': "Ви вже використовували цей пароль раніше. Придумайте новий.",
            'en': "You have used this password before. Please create a new one.",
            'pl': "Używałeś już tego hasła. Wymyśl nowe."
        }
    }
    return msgs.get(key, {}).get(lang, msgs.get(key, {}).get('uk'))

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
                t_val('same_as_current'),
                code='password_reuse',
            )

        # 2. Перевірка: чи не співпадає зі СТАРИМИ паролями з історії
        history = PasswordHistory.objects.filter(user=user)
        for past_pass in history:
            # check_password безпечно порівнює введений текст із зашифрованим хешем
            if check_password(password, past_pass.password_hash):
                raise ValidationError(
                    t_val('used_before'),
                    code='password_reuse',
                )

    def get_help_text(self):
        return "Пароль не повинен співпадати з вашими попередніми паролями."