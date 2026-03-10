from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        # Генеруємо посилання, яке веде на наш фронтенд React
        return f"https://localhost:5173/confirm-email/{emailconfirmation.key}"