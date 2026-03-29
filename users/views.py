from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings
from rest_framework import viewsets, permissions
from .models import UserIngredient
from .serializers import UserIngredientSerializer

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    # Це посилання, на яке Google поверне юзера після підтвердження (його налаштує фронтендер у React)
    callback_url = f"{settings.FRONTEND_URL}/login/callback/"

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

# ================= ВІРТУАЛЬНИЙ ХОЛОДИЛЬНИК (ІНВЕНТАР) =================
class UserIngredientViewSet(viewsets.ModelViewSet):
    serializer_class = UserIngredientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Юзер бачить тільки свій холодильник
        return UserIngredient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # При збереженні автоматично прив'язуємо інгредієнт до поточного юзера
        serializer.save(user=self.request.user)