from django.urls import path
from notes.views import note as note_views

app_name = "notes" 

urlpatterns = [
    path("", note_views.index, name="note_index"),
    path("create/", note_views.create, name="note_create"),
    path("<int:note_id>/edit/", note_views.edit, name="note_update"),
    path("<int:note_id>/delete-ajax/", note_views.delete, name="note_delete_ajax"),
]
