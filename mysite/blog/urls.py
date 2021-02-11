from django.urls import path
from blog import views
urlpatterns = [
    path("", views.index, name="index"),
    path("blog-view/", views.blog_view, name="blog-view"),
]
