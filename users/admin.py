from django.contrib import admin
from .models import CustomUser, UserIngredient

class UserIngredientInline(admin.TabularInline):
    model = UserIngredient
    extra = 1

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'is_email_verified', 'is_staff', 'is_superuser')
    ordering = ('email',)
    search_fields = ('email', 'first_name')
    list_filter = ('is_staff', 'is_superuser')
    filter_horizontal = ('groups', 'user_permissions')

    # Підключаємо інвентар до сторінки юзера
    inlines = [UserIngredientInline]

    # 1. ЗАХИСТ ВІДОБРАЖЕННЯ: Звичайні адміни не будуть бачити Суперадмінів у списку взагалі
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            # Виключаємо всіх суперадмінів з видачі
            return qs.exclude(is_superuser=True)
        return qs

    # 2. ЗАХИСТ РЕДАГУВАННЯ: Хто кого може змінювати
    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser and obj:
            # Звичайний адмін не може міняти суперадміна
            if obj.is_superuser:
                return False
            # Звичайний адмін не може міняти іншого адміністратора (але може змінювати свій власний профіль)
            if obj.groups.filter(name='Administrators').exists() and obj != request.user:
                return False
        return True

    # 3. ЗАХИСТ ВИДАЛЕННЯ: Хто кого може видаляти
    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser and obj:
            if obj.is_superuser:
                return False
            # Звичайний адмін не може видаляти інших адміністраторів
            if obj.groups.filter(name='Administrators').exists():
                return False
        return True