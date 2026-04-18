from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models.recipe import Recipe
from .models.ingredient import Ingredient

# Сигнал для видалення картинки Рецепту
@receiver(post_delete, sender=Recipe)
def delete_recipe_image_on_s3(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)

# Сигнал для видалення картинки Інгредієнта
@receiver(post_delete, sender=Ingredient)
def delete_ingredient_image_on_s3(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)