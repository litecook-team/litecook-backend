from django.db import models
from django.conf import settings

class FavoriteRecipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE, related_name='favorited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Favorite Recipe (Улюблений рецепт)"
        verbose_name_plural = "Favorite Recipes (Улюблені рецепти)"
        unique_together = ('user', 'recipe')

    def __str__(self):
        return f"{self.user.email} - {self.recipe.title}"