from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Назва інгредієнта")

    is_seasonal = models.BooleanField(default=False, verbose_name="Сезонний продукт")

    image = models.ImageField(upload_to='ingredients/images/', blank=True, null=True, verbose_name="Фото інгредієнта")

    # JSONField для зберігання списку чисел
    seasonal_months = models.JSONField(default=list, blank=True, verbose_name="Сезонні місяці (1-12)")

    class Meta:
        verbose_name = "Інгредієнт"
        verbose_name_plural = "Інгредієнти"

    def __str__(self):
        return self.name