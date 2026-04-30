from django.contrib import admin
from django.utils.html import format_html
from .models import CustomUser, UserIngredient, UserActivityLog, UnverifiedUser, SiteSettings
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
    list_display = ('email', 'first_name', 'is_ai_allowed', 'is_online', 'is_email_verified','date_joined', 'is_staff', 'is_banned', 'is_superuser')
    list_editable = ('is_ai_allowed',)
    ordering = ('-date_joined',)
    search_fields = ('email', 'first_name')
    list_filter = ('is_ai_allowed', 'is_banned', 'is_staff', 'is_superuser')
    filter_horizontal = ('groups', 'user_permissions')

    # Підключаємо інвентар до сторінки юзера
    inlines = [UserIngredientInline, UserActivityLogInline]

    # 1. ЗАХИСТ ВІДОБРАЖЕННЯ ТА РОЗДІЛЕННЯ:
    def get_queryset(self, request):
        # Одразу фільтруємо так, щоб показувати ТІЛЬКИ підтверджених
        qs = super().get_queryset(request).filter(is_email_verified=True)

        if not request.user.is_superuser:
            # Виключаємо всіх суперадмінів з видачі для звичайних адмінів
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
    actions = ['force_logout_user', 'ban_user', 'enable_ai_access', 'disable_ai_access']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональна інформація',
         {'fields': ('first_name', 'avatar', 'dietary_preferences', 'allergies', 'favorite_cuisines')}),
        ('Активність', {'fields': ('date_joined', 'is_email_verified', 'last_activity')}),

        # === БЛОК ДЛЯ ШІ ===
        ('🤖 ІНДИВІДУАЛЬНІ НАЛАШТУВАННЯ ШІ', {
            'fields': ('is_ai_allowed', 'ai_provider_override', 'gemini_api_key_override', 'gemini_model_override'),
            'classes': ('collapse',),  # Буде згорнутим за замовчуванням, щоб не заважати
            'description': "Якщо залишити ці поля порожніми, для користувача будуть застосовані ГЛОБАЛЬНІ налаштування сайту."
        }),

        ('УПРАВЛІННЯ БЛОКУВАННЯМ', {
            'fields': ('is_banned', 'banned_until', 'ban_reason'),
            'classes': ('collapse',),
            'description': "Для довічного бану просто поставте галочку. Для тимчасового - вкажіть дату."
        }),
        ('Дозволи', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    readonly_fields = ('date_joined', 'last_activity',)

    # --- ДІЇ АДМІНА ---
    @admin.action(description="✨ Увімкнути ШІ для обраних")
    def enable_ai_access(self, request, queryset):
        queryset.update(is_ai_allowed=True)
        self.message_user(request, "Доступ до ШІ успішно надано.")

    @admin.action(description="🚫 Вимкнути ШІ для обраних")
    def disable_ai_access(self, request, queryset):
        queryset.update(is_ai_allowed=False)
        self.message_user(request, "Доступ до ШІ успішно закрито.")

    @admin.action(description="⛔ Заблокувати обраних користувачів")
    def ban_user(self, request, queryset):
        queryset.update(is_banned=True, ban_reason="Блокування адміністратором")
        self.force_logout_user(request, queryset)
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
            self.message_user(request, "Помилка (впевніться що token_blacklist встановлено у settings.py)",
                              level='error')

@admin.register(UnverifiedUser)
class UnverifiedUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'date_joined')
    ordering = ('-date_joined',)
    actions = ['delete_selected'] # Дозволяємо лише видаляти

    # ОСНОВНА МАГІЯ: Фільтруємо так, щоб тут показувало ТІЛЬКИ непідтверджених
    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_email_verified=False)

    # Забороняємо створювати юзерів через цю "віртуальну" таблицю
    def has_add_permission(self, request):
        return False


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    # Виводимо всі поля
    list_display = ('id', 'is_ai_enabled', 'ai_provider', 'gemini_api_key_choice', 'gemini_model')

    # Робимо їх редагованими прямо зі списку!
    list_editable = ('is_ai_enabled', 'ai_provider', 'gemini_api_key_choice', 'gemini_model')

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()  # Заборонити створювати більше одного налаштування


# ================= МАГІЯ СОРТУВАННЯ ТА ПЕРЕКЛАДУ АДМІНКИ =================
from django.contrib import admin


def get_app_list(self, request, app_label=None):
    """
    Кастомне сортування додатків та моделей в адмін-панелі,
    а також перейменування стандартних додатків.
    """
    app_dict = self._build_app_dict(request, app_label)
    app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

    # 1. Сортуємо самі додатки (Блоки)
    app_ordering = {
        'users': 1,
        'recipes': 2,
        'auth': 3,  # Groups
        'account': 4,  # Email addresses
        'authtoken': 5,  # Tokens
        'token_blacklist': 6,  # Blacklisted tokens
        'socialaccount': 7,  # Social accounts
        'sites': 8,
    }
    app_list.sort(key=lambda x: app_ordering.get(x['app_label'], 999))

    # === НОВЕ: Перейменовуємо стандартні блоки ===
    app_renames = {
        'auth': '3. Authentication (Дозволи та Ролі)',
        'account': '4. Accounts (Електронні адреси)',
        'authtoken': '5. Auth Tokens (Ключі доступу)',
        'token_blacklist': '6. Token Blacklist (Заблоковані ключі)',
        'socialaccount': '7. Social Accounts (Вхід через соцмережі)',
        'sites': '8. Sites (Сайти)'
    }

    # 2. Сортуємо моделі всередині блоків і застосовуємо нові назви
    model_ordering = {
        # Блок Users
        'CustomUser': 1,
        'UnverifiedUser': 2,
        'SiteSettings': 3,

        # Блок Recipes
        'Recipe': 1,
        'Ingredient': 2,
        'RecipeOfDay': 3,
        'WeeklyMenu': 4,
        'FavoriteRecipe': 5,
    }

    for app in app_list:
        # Перейменовуємо великий синій заголовок, якщо він є в нашому словнику
        if app['app_label'] in app_renames:
            app['name'] = app_renames[app['app_label']]

        # Сортуємо моделі всередині
        app['models'].sort(key=lambda x: model_ordering.get(x['object_name'], 999))

    return app_list


# Підміняємо стандартний метод Django на наш кастомний
admin.AdminSite.get_app_list = get_app_list