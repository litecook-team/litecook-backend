from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class WeeklyMenu(models.Model):
    DAY_CHOICES = (
        (1, 'Понеділок'), (2, 'Вівторок'), (3, 'Середа'),
        (4, 'Четвер'), (5, 'П\'ятниця'), (6, 'Субота'), (7, 'Неділя'),
    )
    MEAL_CHOICES = (
        ('breakfast', 'Сніданок'),
        ('lunch', 'Обід'),
        ('dinner', 'Вечеря'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weekly_menus', verbose_name="Користувач")
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE, verbose_name="Рецепт")
    day_of_week = models.IntegerField(choices=DAY_CHOICES, verbose_name="День тижня")
    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES, verbose_name="Прийом їжі")

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Тижневе меню"
        # Користувач не може додати два різні рецепти на один і той самий прийом їжі в один день
        unique_together = ('user', 'day_of_week', 'meal_type')

    def __str__(self):
        return f"{self.user.email} - {self.get_day_of_week_display()} ({self.get_meal_type_display()})"