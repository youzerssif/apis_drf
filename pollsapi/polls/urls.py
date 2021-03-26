from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'polls'
urlpatterns = [
    path("article/", views.article_list, name="article_list"),
    path("article/<int:pk>/", views.article_detail, name="article_detail")

]