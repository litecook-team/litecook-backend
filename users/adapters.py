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
        # Отримуємо згенероване посилання
        activate_url = self.get_email_confirmation_url(request, emailconfirmation)

        # Передаємо посилання в наш HTML-шаблон
        context = {
            'activate_url': activate_url,
        }

        # Рендеримо HTML
        html_content = render_to_string('registration/email_confirmation_message.html', context)

        # Текстова версія (якщо пошта юзера не підтримує HTML)
        text_content = f"Вітаємо у LITE cook!\nДякуємо за реєстрацію. Підтвердіть свою електронну пошту: {activate_url}"

        # Відправляємо лист!
        msg = EmailMultiAlternatives(
            subject="Підтвердження реєстрації у LITE cook",
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[emailconfirmation.email_address.email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()