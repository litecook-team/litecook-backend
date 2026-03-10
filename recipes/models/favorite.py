from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class FavoriteRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE, related_name='favorited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Улюблений рецепт"
        verbose_name_plural = "Улюблені рецепти"
        unique_together = ('user', 'recipe') # Один юзер не може додати один рецепт двічі

    def __str__(self):
        return f"{self.user.email} - {self.recipe.title}"