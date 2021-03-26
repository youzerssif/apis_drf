from django.contrib import admin
from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter
from .apiviews import *


router = DefaultRouter()
router.register(r'utilisateur', UtilisateurViewSet, basename='utilisateur')
router.register(r'categories', CategorieViewSet, basename='categories')
router.register(r'articles', ArticleViewSet, basename='articles')
router.register(r'commentaires', CommentaireViewSet, basename='commentaires')

app_name = 'polls'
urlpatterns = [
    path("article/", views.article_list, name="article_list"),
    path("article/<int:pk>/", views.article_detail, name="article_detail")

]
urlpatterns += router.urls