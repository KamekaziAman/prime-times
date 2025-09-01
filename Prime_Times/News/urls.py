from django.contrib import admin
from django.urls import path
from News import views


urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create_news, name="create_news"),
    path("edit/<int:post_id>/", views.edit_news, name="edit_news"),
    path("read/<int:post_id>/", views.read_page, name="read_news"),
    path("delete/<int:post_id>/", views.delete_news, name="delete_news"),
]
