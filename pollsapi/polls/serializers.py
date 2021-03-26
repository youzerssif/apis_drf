from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin

from . import models


 
class UtilisateurSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    
    class Meta:
        model = models.Utilisateur
        fields = '__all__'
        depth=1
        
               
class CommentaireSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = models.Commentaire
        fields = '__all__'
        depth = 1
        
class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    Commentaire = CommentaireSerializer(many=True, required=False)

    class Meta:
        model = models.Article
        fields = '__all__'
        depth = 1
        
        
class CategorieSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    Article = ArticleSerializer(many=True, required=False)
    
    class Meta:
        model = models.Categorie
        fields = '__all__'
        