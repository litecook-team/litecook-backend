"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Всі запити, що починаються з /api/recipes/, підуть у наш додаток
    path('api/recipes/', include('recipes.urls')),

    # АУТЕНТИФІКАЦІЯ (JWT, Логін, Реєстрація, Підтвердження пошти)
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),

    path('api/auth/password/reset/confirm/<uidb64>/<token>/',
         RedirectView.as_view(url=f"{settings.FRONTEND_URL}/reset-password-confirm/%(uidb64)s/%(token)s/", permanent=False),
         name='password_reset_confirm'),

    # шляхи для соцмереж
    path('api/auth/social/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)