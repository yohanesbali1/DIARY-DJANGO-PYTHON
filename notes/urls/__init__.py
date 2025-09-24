from django.urls import path, include

urlpatterns = [
    path("notes/",  include(("notes.urls.notes", "notes"), namespace="notes")),
]