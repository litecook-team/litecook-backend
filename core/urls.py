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
import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView, TemplateView
from django.http import HttpResponse

# Зібрали імпорти з users.views в один рядок
from users.views import CustomRegisterView, CustomVerifyEmailView
from recipes.models.recipe import Recipe  # Імпортуємо модель рецепту


# ================= КАСТОМНЕ VIEW ДЛЯ OPEN GRAPH =================
def react_app_view(request, recipe_id=None):
    """
    Віддає React-додаток (index.html) з динамічними Open Graph тегами.
    """
    # Шлях до зібраного React index.html.
    # Замініть 'dist' на вашу папку з фронтендом, якщо вона називається інакше
    index_file_path = os.path.join(settings.BASE_DIR, 'dist', 'index.html')

    try:
        with open(index_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        return HttpResponse("Frontend index.html not found.", status=404)

    # Стандартні значення (якщо рецепт не знайдено)
    og_title = "LITE cook - Ваш кулінарний помічник"
    og_description = "Знайдіть ідеальний рецепт за інгредієнтами з вашого холодильника."
    og_image = f"{request.scheme}://{request.get_host()}/static/default_og.jpg"  # Картинка за замовчуванням
    og_url = request.build_absolute_uri()

    # Якщо запит йде на конкретний рецепт
    if recipe_id:
        try:
            recipe = Recipe.objects.get(id=recipe_id)
            og_title = recipe.title

            # Обрізаємо опис до 200 символів (стандарт для месенджерів)
            description = recipe.description or ""
            og_description = (description[:197] + '...') if len(description) > 200 else description

            if recipe.image:
                og_image = request.build_absolute_uri(recipe.image.url)
        except Recipe.DoesNotExist:
            pass

            # Замінюємо плейсхолдери в HTML-файлі
    html_content = html_content.replace('__OG_TITLE__', og_title)
    html_content = html_content.replace('__OG_DESCRIPTION__', og_description)
    html_content = html_content.replace('__OG_IMAGE__', og_image)
    html_content = html_content.replace('__OG_URL__', og_url)

    return HttpResponse(html_content)

# ===============================================================

urlpatterns = [
    # Пастки для ботів та стандартної адмінки
    path('', TemplateView.as_view(template_name='warning.html'), name='home-warning'),
    path('admin/', TemplateView.as_view(template_name='warning.html')),

    # Дозволяємо переходити за посиланням на рецепт, щоб віддавати OG-теги
    path('recipe/<int:recipe_id>/', react_app_view, name='react_recipe_share'),
    path('recipe/<int:recipe_id>', react_app_view), # Дубль без слеша на кінці
    # ==============================================

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