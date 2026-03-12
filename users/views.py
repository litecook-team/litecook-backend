from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    # Це посилання, на яке Google поверне юзера після підтвердження (його налаштує фронтендер у React)
    callback_url = f"{settings.FRONTEND_URL}/login/callback/"

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter