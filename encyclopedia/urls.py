from django.urls import path
from . import util
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("new_page", views.new_page, name="new_page"),
    path("random_page", views.random_page, name="random_page"),
    path("edit", views.edit, name="edit"),
    path("search", views.search, name="search"),
    path("<str:title>", views.title, name="title"),
]
