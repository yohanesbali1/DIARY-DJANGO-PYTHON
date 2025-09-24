from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponseForbidden
from django.contrib.auth import logout

class RedirectLoggedInMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        protected_paths = [reverse("login"), reverse("register")]

        if request.user.is_authenticated and request.path in protected_paths:
            return redirect("notes:note_index")

        return self.get_response(request)

class Redirect403Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Jika 403, arahkan ke login page
        if isinstance(response, HttpResponseForbidden):
            logout(request)
            return redirect(settings.LOGIN_URL)

        return response