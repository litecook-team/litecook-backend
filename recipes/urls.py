from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IngredientViewSet, RecipeViewSet, FavoriteViewSet, WeeklyMenuViewSet, AIChatView
from users.views import UserIngredientViewSet

# Роутер автоматично створює шляхи для GET, POST, PUT, DELETE запитів
router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'favorites', FavoriteViewSet, basename='favorite')
router.register(r'weekly-menu', WeeklyMenuViewSet, basename='weekly-menu')
router.register(r'inventory', UserIngredientViewSet, basename='inventory')

urlpatterns = [
    # === НАШ НОВИЙ ШЛЯХ ДЛЯ ШІ ===
    # Він оброблятиме POST запити на /api/ai-chat/
    path('ai-chat/', AIChatView.as_view(), name='ai-chat'),

    path('', include(router.urls)),
]