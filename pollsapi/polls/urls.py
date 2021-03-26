from django.contrib import admin
from django.urls import path,include, re_path
from . import views

from rest_framework.routers import DefaultRouter
from .apiviews import *


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'utilisateur', UtilisateurViewSet, basename='utilisateur')
router.register(r'categories', CategorieViewSet, basename='categories')
router.register(r'articles', ArticleViewSet, basename='articles')
router.register(r'commentaires', CommentaireViewSet, basename='commentaires')

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name = 'polls'
urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    ######### Pure APIs
    path("article/", views.article_list, name="article_list"),
    path("article/<int:pk>/", views.article_detail, name="article_detail")

]
urlpatterns += router.urls