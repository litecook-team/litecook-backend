from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from users.models import CustomUser
from dj_rest_auth.serializers import PasswordResetSerializer
from django.conf import settings

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from dj_rest_auth.serializers import PasswordResetConfirmSerializer
from django.utils.http import urlsafe_base64_decode


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

class CustomPasswordResetConfirmSerializer(PasswordResetConfirmSerializer):
    def validate(self, attrs):
        uid = attrs.get('uid')
        token = attrs.get('token')

        # 1. Безпечно розшифровуємо ID користувача
        try:
            uid_decoded = force_str(urlsafe_base64_decode(uid))
            user = CustomUser.objects.get(pk=uid_decoded)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            raise serializers.ValidationError({"uid": ["Недійсне посилання або користувач не існує."]})

        # 2. Перевіряємо, чи токен ще дійсний
        if not default_token_generator.check_token(user, token):
            raise serializers.ValidationError({"token": ["Посилання застаріло або вже було використане. Надішліть новий запит."]})

        # 3. Перевіряємо, чи співпадають паролі
        if attrs.get('new_password1') != attrs.get('new_password2'):
            raise serializers.ValidationError({"non_field_errors": ["Паролі не співпадають."]})

        # 4. Перевіряємо надійність пароля (щоб не був "12345678" чи схожим на email)
        from django.contrib.auth.password_validation import validate_password
        from django.core.exceptions import ValidationError as DjangoValidationError
        try:
            validate_password(attrs['new_password1'], user)
        except DjangoValidationError as e:
            raise serializers.ValidationError({"new_password1": list(e.messages)})

        self.user = user
        return attrs

    def save(self, **kwargs):
        # Надійно зберігаємо новий пароль у базу даних
        self.user.set_password(self.validated_data['new_password1'])
        self.user.save()
        return self.user