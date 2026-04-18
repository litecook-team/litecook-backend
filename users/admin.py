from django.contrib import admin
from django.utils.html import format_html
from .models import CustomUser, UserIngredient, UserActivityLog
from rest_framework_simplejwt.tokens import OutstandingToken

class UserIngredientInline(admin.TabularInline):
    model = UserIngredient
    extra = 1

# ТАБЛИЦЯ СЕСІЙ В ПРОФІЛІ
class UserActivityLogInline(admin.TabularInline):
    model = UserActivityLog
    extra = 0
    can_delete = False
    max_num = 0
    readonly_fields = ('device_info', 'ip_address', 'country', 'last_endpoint', 'last_seen', 'is_active_session')
    fields = ('device_info', 'ip_address', 'country', 'last_endpoint', 'last_seen', 'is_active_session')

    def device_info(self, obj):
        icon = "📱" if obj.device_type == 'Mobile' else "💻" if obj.device_type == 'PC' else "🖥️"
        return f"{icon} {obj.os} / {obj.browser}"
    device_info.short_description = "Пристрій"

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'is_online', 'is_email_verified','date_joined', 'is_staff', 'is_banned', 'is_superuser')
    ordering = ('-date_joined',)
    search_fields = ('email', 'first_name')
    list_filter = ('is_banned', 'is_staff', 'is_superuser')
    filter_horizontal = ('groups', 'user_permissions')

    # Підключаємо інвентар до сторінки юзера
    inlines = [UserIngredientInline, UserActivityLogInline]

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

    # КНОПКИ УПРАВЛІННЯ
    actions = ['force_logout_user', 'ban_user']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональна інформація', {'fields': ('first_name', 'avatar', 'dietary_preferences', 'allergies', 'favorite_cuisines')}),
        ('Активність', {'fields': ('date_joined', 'is_email_verified', 'last_activity')}),
        ('УПРАВЛІННЯ БЛОКУВАННЯМ', {
            'fields': ('is_banned', 'banned_until', 'ban_reason'),
            'classes': ('collapse',),
            'description': "Для довічного бану просто поставте галочку. Для тимчасового - вкажіть дату."
        }),
        ('Дозволи', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    readonly_fields = ('date_joined', 'last_activity',)

    # --- ДІЇ АДМІНА ---
    @admin.action(description="⛔ Заблокувати обраних користувачів")
    def ban_user(self, request, queryset):
        queryset.update(is_banned=True, ban_reason="Блокування адміністратором")
        self.force_logout_user(request, queryset) # Одразу викидаємо їх з сайту
        self.message_user(request, "Користувачів заблоковано та викинуто з сесій.")

    @admin.action(description="🔌 Примусово викинути з профілю (Анулювати токени)")
    def force_logout_user(self, request, queryset):
        try:
            from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
            for user in queryset:
                tokens = OutstandingToken.objects.filter(user=user)
                for token in tokens:
                    BlacklistedToken.objects.get_or_create(token=token)
                UserActivityLog.objects.filter(user=user).update(is_active_session=False)
            self.message_user(request, "Сесії успішно анульовані.")
        except Exception as e:
            self.message_user(request, "Помилка (впевніться що token_blacklist встановлено у settings.py)", level='error')