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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.generic import TemplateView

# Зібрали імпорти з users.views в один рядок
from users.views import CustomRegisterView, CustomVerifyEmailView

urlpatterns = [
    # Пастки для ботів та стандартної адмінки
    path('', TemplateView.as_view(template_name='warning.html'), name='home-warning'),
    path('admin/', TemplateView.as_view(template_name='warning.html')),

    # Наша секретна адмінка
    path(settings.ADMIN_URL, admin.site.urls),

    # Маршрути рецептів (додаток recipes)
    path('api/', include('recipes.urls')),

    # =========================================================
    # АУТЕНТИФІКАЦІЯ (JWT, Логін, Реєстрація, Підтвердження)
    # =========================================================

    # 1. Перехоплення скидання пароля (Фронтенд-посередник)
    path('api/auth/password/reset/confirm/<uidb64>/<token>/',
         RedirectView.as_view(url=f"{settings.FRONTEND_URL}/reset-password-confirm/%(uidb64)s/%(token)s/",
                              permanent=False),
         name='password_reset_confirm'),

    # 2. НАШІ КАСТОМНІ ЕНДПОІНТИ (ОБОВ'ЯЗКОВО ВИЩЕ СТАНДАРТНИХ!)
    # Перехоплюємо верифікацію пошти, щоб видавати токени (Магія автовходу)
    path('api/auth/registration/verify-email/', CustomVerifyEmailView.as_view(), name='custom_verify_email'),
    # Перехоплюємо реєстрацію для захисту від ботів
    path('api/auth/registration/', CustomRegisterView.as_view(), name='custom_register'),

    # 3. СТАНДАРТНІ ЕНДПОІНТИ dj-rest-auth
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),

    # 4. Шляхи для соцмереж (Google, Facebook)
    path('api/auth/social/', include('users.urls')),
]

# Налаштування для медіа-файлів у режимі розробки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# === ГОЛОВНА ПАСТКА (ЗАВЖДИ В САМОМУ КІНЦІ) ===
# Перехоплює будь-які URL, які не підійшли під жоден з маршрутів вище.
urlpatterns.append(re_path(r'^.*$', TemplateView.as_view(template_name='warning.html')))