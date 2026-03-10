from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models.favorite import FavoriteRecipe
from .models.weekly_menu import WeeklyMenu
from .models.ingredient import Ingredient
from .models.recipe import Recipe
from .serializers import IngredientSerializer, RecipeSerializer, FavoriteSerializer, WeeklyMenuSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    # Додаємо модулі фільтрації та пошуку
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # 1. Точна фільтрація (наприклад, вивести тільки рецепти з певним тегом)
    filterset_fields = ['dietary_tags', 'cooking_time']

    # 2. Розумний текстовий пошук (шукаємо по назві та опису обома мовами)
    search_fields = ['title', 'title_en', 'description', 'description_en']

    # 3. Сортування (наприклад, від найшвидших до найдовших)
    ordering_fields = ['cooking_time', 'calories']

    # Робимо API доступним для читання всім, а змінювати можуть тільки адміни
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated] # Доступ ТІЛЬКИ для залогінених

    def get_queryset(self):
        # Юзер бачить тільки свої лайки
        return FavoriteRecipe.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Коли юзер лайкає рецепт, ми автоматично записуємо його ID в базу
        serializer.save(user=self.request.user)

class WeeklyMenuViewSet(viewsets.ModelViewSet):
    serializer_class = WeeklyMenuSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WeeklyMenu.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)