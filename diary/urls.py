"""
URL configuration for diary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
from django.urls import path,include
from notes.views import auth
from django.conf.urls import handler404
from django.shortcuts import render

urlpatterns = [
       # Auth
    path("login/", auth.login_view, name="login"),
    path("logout/", auth.logout_view, name="logout"),
    path("register/", auth.register_view, name="register"),

    # Notes CRUD
    path('', include(("notes.urls.notes", "notes"), namespace="notes")),
]

def custom_404_view(request, exception):
    return render(request, "errors/404.html", status=404)

handler404 = custom_404_view