from django.apps import AppConfig


class RecipesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipes'
    verbose_name = '2. Recipes (Кулінарна база)'

    def ready(self):
        import recipes.signals  # noqa Імпортуємо файл із сигналами при старті додатку
