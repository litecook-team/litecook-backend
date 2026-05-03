from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from .models import CustomUser, UserIngredient
from dj_rest_auth.serializers import PasswordResetSerializer
from django.conf import settings
import requests

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from dj_rest_auth.serializers import PasswordResetConfirmSerializer
from django.utils.http import urlsafe_base64_decode

def get_lang(serializer_instance):
    request = serializer_instance.context.get('request')
    return getattr(request, 'LANGUAGE_CODE', 'uk')[:2] if request else 'uk'

# === ФУНКЦІЯ ДЛЯ ПРОСТОГО ПЕРЕКЛАДУ ПОМИЛОК ===
def t_msg(key, request):
    lang = getattr(request, 'LANGUAGE_CODE', 'uk')[:2] if request else 'uk'
    msgs = {
        'not_found': {
            'uk': "Користувача з такою електронною поштою не знайдено.",
            'en': "User with this email not found.",
            'pl': "Użytkownik z tym e-mailem nie został znaleziony."
        },
        'social_acc': {
            'uk': "Цей акаунт був зареєстрований через соціальні мережі (Google/Facebook). Для входу скористайтеся відповідною кнопкою на сторінці авторизації.",
            'en': "This account was registered via social networks (Google/Facebook). Please use the corresponding button to log in.",
            'pl': "To konto zostało zarejestrowane przez sieci społecznościowe (Google/Facebook). Użyj odpowiedniego przycisku, aby się zalogować."
        },
        'invalid_link': {
            'uk': "Недійсне посилання або користувач не існує.",
            'en': "Invalid link or user does not exist.",
            'pl': "Nieprawidłowy link lub użytkownik nie istnieje."
        },
        'invalid_captcha': {
            'uk': "Перевірка на робота не пройдена. Оновіть сторінку і спробуйте ще раз.",
            'en': "Robot verification failed. Refresh the page and try again.",
            'pl': "Weryfikacja robota nie powiodła się. Odśwież stronę i spróbuj ponownie."
        },
        'captcha_conn_err': {
            'uk': "Помилка з'єднання з сервером перевірки CAPTCHA. Спробуйте пізніше.",
            'en': "Connection error with CAPTCHA verification server. Try again later.",
            'pl': "Błąd połączenia z serwerem weryfikacji CAPTCHA. Spróbuj ponownie później."
        },
        'token_expired': {
            'uk': "Посилання застаріло або вже було використане. Надішліть новий запит.",
            'en': "The link has expired or has already been used. Please submit a new request.",
            'pl': "Link wygasł lub został już użyty. Wyślij nowe żądanie."
        },
        'pass_mismatch': {
            'uk': "Паролі не співпадають.",
            'en': "Passwords do not match.",
            'pl': "Hasła nie pasują do siebie."
        }
    }
    return msgs.get(key, {}).get(lang, msgs.get(key, {}).get('uk'))


class CustomRegisterSerializer(RegisterSerializer):
    # 1. Прибираємо поле username з форми
    username = None
    # 2. Додаємо наше обов'язкове поле Ім'я
    first_name = serializers.CharField(max_length=70, required=True, label="Ім'я")

    # записується тільки при прийомі даних (write_only)
    captcha_token = serializers.CharField(write_only=True, required=True, label="Captcha Token")

    # метод примусово змінює порядок полів у формі
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Вказуємо бажаний порядок
        field_order = ['first_name', 'email', 'password1', 'password2', 'captcha_token']
        # Перезбираємо словник полів у новому порядку
        self.fields = {key: self.fields[key] for key in field_order if key in self.fields}

    # Використовуємо загальний метод validate для надійності
    def validate(self, data):
        # 1. Викликаємо стандартну валідацію (паролі, пошта тощо)
        validated_data = super().validate(data)

        # 2. Витягуємо токен каптчі
        captcha_token = data.get('captcha_token')
        request = self.context.get('request')

        if not captcha_token:
            raise serializers.ValidationError(t_msg('invalid_captcha', request))

        # 3. Перевіряємо токен через Google API
        secret_key = settings.RECAPTCHA_SECRET_KEY
        verify_url = 'https://www.google.com/recaptcha/api/siteverify'

        payload = {
            'secret': secret_key,
            'response': captcha_token
        }

        try:
            response = requests.post(verify_url, data=payload)
            result = response.json()

            if not result.get('success'):
                raise serializers.ValidationError(t_msg('invalid_captcha', request))
        except requests.exceptions.RequestException:
            raise serializers.ValidationError(t_msg('captcha_conn_err', request))

        # 4. Якщо все добре, повертаємо дані (але без токена, бо в базу його зберігати не треба)
        validated_data.pop('captcha_token', None)
        return validated_data

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


class UserIngredientSerializer(serializers.ModelSerializer):
    # === Замість ReadOnlyField використовуємо SerializerMethodField для динамічного перекладу
    ingredient_name = serializers.SerializerMethodField()
    ingredient_image = serializers.ImageField(source='ingredient.image', read_only=True)

    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = UserIngredient
        fields = ('id', 'ingredient', 'ingredient_name', 'ingredient_image', 'amount', 'unit', 'created_at',
                  'updated_at')

    # === логіка вибору правильної колонки (name_en або name_pl)
    def get_ingredient_name(self, obj):
        lang = get_lang(self)
        if lang == 'en' and obj.ingredient.name_en:
            return obj.ingredient.name_en
        if lang == 'pl' and obj.ingredient.name_pl:
            return obj.ingredient.name_pl
        return obj.ingredient.name

class CustomUserDetailsSerializer(UserDetailsSerializer):
    # кастомне поле для лічильника
    favorites_count = serializers.SerializerMethodField()
    # поле для інвентарю
    inventory = UserIngredientSerializer(many=True, read_only=True)

    has_usable_password = serializers.SerializerMethodField()

    class Meta(UserDetailsSerializer.Meta):
        model = CustomUser
        fields = ('pk', 'email', 'first_name', 'avatar', 'dietary_preferences', 'allergies', 'favorite_cuisines',
                  'is_staff', 'is_superuser', 'favorites_count', 'inventory', 'has_usable_password')
        read_only_fields = ('email', 'is_staff', 'is_superuser', 'favorites_count', 'inventory', 'has_usable_password')

    # Метод, який рахує кількість улюблених рецептів
    def get_favorites_count(self, obj):
        # Звертаємося до related_name 'favorites' з моделі FavoriteRecipe
        return obj.favorites.count()

    def get_has_usable_password(self, obj):
        return obj.has_usable_password()


class CustomPasswordResetSerializer(PasswordResetSerializer):
    def validate_email(self, value):
        request = self.context.get('request')
        # 1. ПЕРЕВІРКА: Чи існує користувач з такою поштою?
        user = CustomUser.objects.filter(email=value).first()
        if not user:
            # викидаємо помилку з ключем 'email', яку фронтенд очікує і вміє обробляти.
            raise serializers.ValidationError(t_msg('not_found', request))

        # 2. ПЕРЕВІРКА: Чи має користувач встановлений пароль (чи це соц. акаунт)?
        if not user.has_usable_password():
            raise serializers.ValidationError(t_msg('social_acc', request))

        return value

    def save(self):
        # Оскільки ми вже пройшли валідацію, ми точно знаємо, що юзер існує
        email = self.validated_data['email']
        user = CustomUser.objects.get(email=email)

        # Генеруємо безпечні ключі для скидання пароля
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        # 1. Отримуємо запит та мову
        request = self.context.get('request')
        lang = getattr(request, 'LANGUAGE_CODE', 'uk')[:2] if request else 'uk'

        context = {
            'frontend_url': settings.FRONTEND_URL,
            'uid': uid,
            'token': token,
            'lang': lang,  # ПЕРЕДАЄМО МОВУ
        }
        html_content = render_to_string('registration/password_reset_email.html', context)
        reset_url = f"{settings.FRONTEND_URL}/reset-password-confirm/{uid}/{token}"

        # 3. Словники для теми та тексту
        subjects = {
            'en': "Password Reset at LITE cook",
            'pl': "Resetowanie hasła w LITE cook",
            'uk': "Відновлення пароля у LITE cook"
        }
        texts = {
            'en': f"Password reset:\nFollow the link: {reset_url}",
            'pl': f"Resetowanie hasła:\nPrzejdź pod link: {reset_url}",
            'uk': f"Відновлення пароля:\nПерейдіть за посиланням: {reset_url}"
        }

        msg = EmailMultiAlternatives(
            subject=subjects.get(lang, subjects['uk']),
            body=texts.get(lang, texts['uk']),
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

class CustomPasswordResetConfirmSerializer(PasswordResetConfirmSerializer):
    def validate(self, attrs):
        request = self.context.get('request')
        uid = attrs.get('uid')
        token = attrs.get('token')

        # 1. Безпечно розшифровуємо ID користувача
        try:
            uid_decoded = force_str(urlsafe_base64_decode(uid))
            user = CustomUser.objects.get(pk=uid_decoded)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            raise serializers.ValidationError({"uid": [t_msg('invalid_link', request)]})

        # 2. Перевіряємо, чи токен ще дійсний
        if not default_token_generator.check_token(user, token):
            raise serializers.ValidationError({"token": [t_msg('token_expired', request)]})

        # 3. Перевіряємо, чи співпадають паролі
        if attrs.get('new_password1') != attrs.get('new_password2'):
            raise serializers.ValidationError({"non_field_errors": [t_msg('pass_mismatch', request)]})

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