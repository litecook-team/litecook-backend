from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from users.models import CustomUser


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