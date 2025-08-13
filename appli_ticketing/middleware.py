from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow unauthenticated access to login, register, password reset, and admin
        allowed_paths = [
            reverse('login'),
            reverse('register'),
            reverse('password_reset'),
            reverse('password_reset_done'),
            reverse('password_reset_confirm', kwargs={'uidb64': 'uidb64', 'token': 'token'}),
            reverse('password_reset_complete'),
            '/admin/',
        ]
        if not request.user.is_authenticated and not any(request.path.startswith(path) for path in allowed_paths):
            return redirect(settings.LOGIN_URL + '?next=' + request.path)
        return self.get_response(request)
