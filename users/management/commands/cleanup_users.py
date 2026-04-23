from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from users.models import CustomUser


class Command(BaseCommand):
    help = 'Видаляє акаунти, які не підтвердили пошту протягом 24 годин'

    def handle(self, *args, **kwargs):
        # Віднімаємо 24 години від поточного часу
        time_threshold = timezone.now() - timedelta(hours=24)

        # Шукаємо юзерів: пошта не підтверджена і зареєструвалися раніше ніж 24 години тому
        users_to_delete = CustomUser.objects.filter(
            is_email_verified=False,
            date_joined__lt=time_threshold
        )

        count = users_to_delete.count()
        users_to_delete.delete()  # Видаляємо їх з бази назавжди

        self.stdout.write(self.style.SUCCESS(f'Успішно видалено непідтверджених акаунтів: {count}'))