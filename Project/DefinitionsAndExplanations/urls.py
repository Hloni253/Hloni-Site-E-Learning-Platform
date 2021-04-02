from django.urls import path
from .views import save_definition, remove_definition, save_explanation, remove_explanation, save_video, remove_video

app_name = 'Definition'
urlpatterns = [
    path("definition/<id>",save_definition,name='Save_Def'),
    path("remove/definition/<id>", remove_definition,name="Remove_Def"),
    path("explanation/<id>",save_explanation,name='Save_Exp'),
    path("remove/explanation/<id>", remove_explanation,name="Remove_Exp"),
    path("video/<id>", save_video,name="Save_Vid"),
    path("remove/video/<id>",remove_video,name="Remove_Vid"),
    ]
