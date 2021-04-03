from rest_framework import viewsets, filters
from .models import *
from .serializers import *
# from .apiviews import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey



class DynamicSearchFilter(filters.SearchFilter):
      def get_search_fields(self, view, request):
          return request.GET.getlist('search_fields', [])


class UtilisateurViewSet(viewsets.ModelViewSet):
      filter_backends = (DynamicSearchFilter,)
      queryset = Utilisateur.objects.all()
      serializer_class = UtilisateurSerializer
      permission_classes = [HasAPIKey]
          

#______________________ CATEGORIE ARTICLE ____________________#
class CategorieViewSet(viewsets.ModelViewSet):
      filter_backends = (DynamicSearchFilter,)
      queryset = Categorie.objects.all()
      serializer_class = CategorieSerializer
      permission_classes = [HasAPIKey]
      

#______________________ ARTICLE_______________________#
class ArticleViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [HasAPIKey]


#______________________ COMMENTAIRE ARTICLE_______________________#
class CommentaireViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    permission_classes = [HasAPIKey]