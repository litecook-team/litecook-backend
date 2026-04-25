from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class CustomAccountAdapter(DefaultAccountAdapter):

    # 1. Посилання для підтвердження пошти при реєстрації
    def get_email_confirmation_url(self, request, emailconfirmation):
        # Використовуємо змінну з settings.py
        return f"{settings.FRONTEND_URL}/confirm-email/{emailconfirmation.key}"

    # 2. Посилання, яке прийде в листі для "Забули пароль?"
    def get_reset_password_from_key_url(self, reset_password_key):
        return f"{settings.FRONTEND_URL}/reset-password-confirm/{reset_password_key}"

    # 3. ВЛАСНА ВІДПРАВКА ЛИСТА ПІДТВЕРДЖЕННЯ З HTML-ДИЗАЙНОМ
    def send_confirmation_mail(self, request, emailconfirmation, signup):
        activate_url = self.get_email_confirmation_url(request, emailconfirmation)

        # 1. Отримуємо мову з заголовків (за замовчуванням 'uk')
        lang = getattr(request, 'LANGUAGE_CODE', 'uk')[:2]

        # 2. Передаємо мову в HTML шаблон
        context = {
            'activate_url': activate_url,
            'frontend_url': settings.FRONTEND_URL,
            'lang': lang,
        }
        html_content = render_to_string('registration/email_confirmation_message.html', context)

        # 3. Словники для теми та тексту (без використання GNU gettext)
        subjects = {
            'en': "Registration Confirmation at LITE cook",
            'pl': "Potwierdzenie rejestracji w LITE cook",
            'uk': "Підтвердження реєстрації у LITE cook"
        }
        texts = {
            'en': f"Welcome to LITE cook!\nConfirm your email: {activate_url}",
            'pl': f"Witamy w LITE cook!\nPotwierdź swój adres e-mail: {activate_url}",
            'uk': f"Вітаємо у LITE cook!\nДякуємо за реєстрацію. Підтвердіть свою електронну пошту: {activate_url}"
        }

        msg = EmailMultiAlternatives(
            subject=subjects.get(lang, subjects['uk']),
            body=texts.get(lang, texts['uk']),
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[emailconfirmation.email_address.email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()