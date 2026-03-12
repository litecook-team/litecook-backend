from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from users.models import CustomUser
from dj_rest_auth.serializers import PasswordResetSerializer
from django.conf import settings

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class CustomRegisterSerializer(RegisterSerializer):
    # 1. Прибираємо поле username з форми
    username = None
    # 2. Додаємо наше обов'язкове поле Ім'я
    first_name = serializers.CharField(max_length=150, required=True, label="Ім'я")

    # Цей метод примусово змінює порядок полів у формі
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Вказуємо бажаний порядок
        field_order = ['first_name', 'email', 'password1', 'password2']
        # Перезбираємо словник полів у новому порядку
        self.fields = {key: self.fields[key] for key in field_order if key in self.fields}

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['first_name'] = self.validated_data.get('first_name', '')
        return data

    def save(self, request):
        # Зберігаємо юзера і додаємо йому ім'я
        user = super().save(request)
        user.first_name = self.cleaned_data.get('first_name')
        user.save()
        return user

class CustomLoginSerializer(LoginSerializer):
    # Примусово прибираємо поле username з форми входу
    username = None

class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        model = CustomUser
        # Додали is_staff та is_superuser, щоб фронтенд розумів ролі
        fields = ('pk', 'email', 'first_name', 'avatar', 'dietary_preferences', 'allergies', 'favorite_cuisines', 'is_staff', 'is_superuser')
        # Робимо їх read_only, щоб хакери не могли самі собі призначити адмінку через API
        read_only_fields = ('email', 'is_staff', 'is_superuser')


class CustomPasswordResetSerializer(PasswordResetSerializer):
    def save(self):
        # Дістаємо email, який ввів користувач на фронтенді
        email = self.validated_data['email']
        user = CustomUser.objects.filter(email=email).first()

        if user:
            # Генеруємо безпечні ключі для скидання пароля
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            # Дані, які ми передамо в наш HTML-шаблон
            context = {
                'frontend_url': settings.FRONTEND_URL,
                'uid': uid,
                'token': token,
            }

            # Генеруємо HTML-версію листа
            html_content = render_to_string('registration/password_reset_email.html', context)

            # Текстова версія (резервна, якщо пошта користувача не підтримує HTML)
            text_content = f"Відновлення пароля:\nПерейдіть за посиланням: {settings.FRONTEND_URL}/reset-password-confirm/{uid}/{token}"

            # ВІДПРАВЛЯЄМО ЛИСТ САМОСТІЙНО!
            msg = EmailMultiAlternatives(
                subject="Відновлення пароля у LITE cook",  # Красива тема листа
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[user.email]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()