from rest_framework import viewsets, filters
from .models import *
from .serializers import *
# from .apiviews import *

class DynamicSearchFilter(filters.SearchFilter):
      def get_search_fields(self, view, request):
          return request.GET.getlist('search_fields', [])


class UtilisateurViewSet(viewsets.ModelViewSet):
      filter_backends = (DynamicSearchFilter,)
      queryset = Utilisateur.objects.all()
      serializer_class = UtilisateurSerializer
          

#______________________ CATEGORIE ARTICLE ____________________#
class CategorieViewSet(viewsets.ModelViewSet):
      filter_backends = (DynamicSearchFilter,)
      queryset = Categorie.objects.all()
      serializer_class = CategorieSerializer
      

#______________________ ARTICLE_______________________#
class ArticleViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


#______________________ COMMENTAIRE ARTICLE_______________________#
class CommentaireViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer