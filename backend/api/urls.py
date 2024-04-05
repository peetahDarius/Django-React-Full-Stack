from . import views
from django.urls import path


urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("note/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
]
