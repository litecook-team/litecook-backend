import requests
from urllib.parse import urlparse  # ІМПОРТ ДЛЯ РОБОТИ З URL
from django.utils import timezone
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from user_agents import parse
from .models import UserActivityLog, CustomUser


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')


def get_country_from_ip(ip):
    if ip in ['127.0.0.1', 'localhost']: return 'Локальна мережа'
    try:
        res = requests.get(f'http://ip-api.com/json/{ip}', timeout=2).json()
        return res.get('country', 'Невідомо')
    except:
        return 'Невідомо'


class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.jwt_auth = JWTAuthentication()

    def __call__(self, request):
        user = request.user

        if not user.is_authenticated:
            try:
                auth_result = self.jwt_auth.authenticate(request)
                if auth_result:
                    user = auth_result[0]
            except Exception:
                pass

        if user and user.is_authenticated:
            if user.is_banned:
                if user.banned_until and user.banned_until <= timezone.now():
                    user.is_banned = False
                    user.banned_until = None
                    user.save(update_fields=['is_banned', 'banned_until'])
                else:
                    return JsonResponse({
                        "detail": "Ваш акаунт заблоковано.",
                        "reason": user.ban_reason
                    }, status=403)

            now = timezone.now()

            if not user.last_activity or (now - user.last_activity).seconds > 60:
                user.last_activity = now
                user.save(update_fields=['last_activity'])

            if not hasattr(request, 'session_logged') or not request.session_logged:
                ip = get_client_ip(request)
                user_agent_string = request.META.get('HTTP_USER_AGENT', '')
                browser_family = parse(user_agent_string).browser.family

                # === РОЗУМНЕ ВИЗНАЧЕННЯ СТОРІНКИ ФРОНТЕНДУ ===
                referer = request.META.get('HTTP_REFERER')
                frontend_path = None

                if referer:
                    # Якщо є Referer, дістаємо з нього тільки шлях (з 'http://localhost:5173/menu' дістане '/menu')
                    parsed_url = urlparse(referer)
                    frontend_path = parsed_url.path
                    # Якщо шлях порожній, значить це головна сторінка
                    if not frontend_path:
                        frontend_path = '/'

                existing_activities = UserActivityLog.objects.filter(
                    user=user,
                    ip_address=ip,
                    browser=browser_family
                )

                if existing_activities.exists():
                    activity = existing_activities.first()

                    # Оновлюємо шлях ТІЛЬКИ якщо ми змогли витягнути реальну сторінку фронтенду
                    if frontend_path:
                        activity.last_endpoint = frontend_path

                    activity.last_seen = now
                    activity.is_active_session = True
                    activity.save()
                else:
                    user_agent = parse(user_agent_string)
                    country = get_country_from_ip(ip)

                    # Якщо Referer чомусь немає при першому запиті, беремо просто шлях API
                    initial_path = frontend_path if frontend_path else request.path

                    UserActivityLog.objects.create(
                        user=user,
                        ip_address=ip,
                        browser=browser_family,
                        os=f"{user_agent.os.family} {user_agent.os.version_string}",
                        device_type='Mobile' if user_agent.is_mobile else 'Tablet' if user_agent.is_tablet else 'PC',
                        country=country,
                        last_endpoint=initial_path,
                        last_seen=now,
                        is_active_session=True
                    )

                request.session_logged = True

        return self.get_response(request)