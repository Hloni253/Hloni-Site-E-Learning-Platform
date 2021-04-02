from django.urls import path
from .views import home, courses, blog, blog_detail, concepts

app_name = "Home"
urlpatterns = [
    path('', home, name="Home"),
    path('courses', courses, name="Courses"),
    path('blog', blog),
    path('detail', blog_detail),
    path('concept/<subject_slug>/<grade_slug>/<topic_slug>/', concepts, name="Concepts"),
    ]
