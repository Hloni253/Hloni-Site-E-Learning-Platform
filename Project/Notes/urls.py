from django.urls import path
from .views import List_Notes, Note_View, Create_Note, Copy_Note, save_note, remove_note

app_name="Notes"

urlpatterns = [
    path('list', List_Notes, name="List"),
    path('view/<id>', Note_View,name="View"),
    path('create/', Create_Note,name="Create"),
    path('copy/<id>', Copy_Note,name="Copy"),
    path('save/<id>', save_note, name="Save"),
    path('remove/<id>', remove_note, name="Remove"),
    ]
