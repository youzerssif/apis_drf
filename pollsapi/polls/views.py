from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from . import models

# Create your views here.


def article_list(request):
    
    article_list = models.Article.objects.filter(status=True).values('titre')
    
    datas = {
        "article_list":list(article_list),
    }
    return JsonResponse(datas)

def article_detail(request, pk):

    article_detail = get_object_or_404(models.Article, pk=pk)
    # print(article_detail)
    
    datas = {
        "results":{
            "categorie":article_detail.categorie.nom,
            "titre":article_detail.titre,
            "image":article_detail.image.url,
            "description":article_detail.description,
            },
    }
    # print(datas)
    return JsonResponse(datas)