from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


# Register your models here.

@admin.register(models.Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('view_image', 'user','adresse','contact', 'date_add', 'date_upd', 'status',)
    list_filter = ('date_add', 'date_upd', 'status',)
    search_field = ('user')
    actions = ('active', 'desactive') 
    def active(self, request, queryset):
        queryset.update(status = True)
        self.message_user(request, 'Activer un Utilisateur')
    active.short_description = 'active Utilisateur'

    def desactive(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver un Utilisateur')
    desactive.short_description = 'desactive Utilisateur'
    ordering = ('user',)
    list_per_page = 100
    date_hierarchy = ('date_add')
    list_display_links = ('view_image', 'user',)

    def view_image(self, obj):
        try:
            return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.photo_profile.url))
        except Exception as e:
            print(e)


@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_add', 'date_upd', 'status',)
    list_filter = ('date_add', 'date_upd', 'status',)
    search_field = ('nom')
    actions = ('active', 'desactive') 
    def active(self, request, queryset):
        queryset.update(status = True)
        self.message_user(request, 'Activer une Categorie')
    active.short_description = 'active Categorie'

    def desactive(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver une Categorie')
    desactive.short_description = 'desactive Categorie'
    ordering = ('nom',)
    list_per_page = 100
    date_hierarchy = ('date_add')
    list_display_links = ('nom',)



@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('view_image', 'titre','categorie', 'date_add', 'date_upd', 'status',)
    list_filter = ('date_add', 'date_upd', 'status','categorie')
    search_field = ('titre')
    actions = ('active', 'desactive') 
    def active(self, request, queryset):
        queryset.update(status = True)
        self.message_user(request, 'Activer un Article')
    active.short_description = 'active Article'

    def desactive(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver un Article')
    desactive.short_description = 'desactive Article'
    ordering = ('titre',)
    list_per_page = 100
    date_hierarchy = ('date_add')
    list_display_links = ('view_image', 'titre',)

    def view_image(self, obj):
        try:
            return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))
        except Exception as e:
            print(e)


@admin.register(models.Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('auteur','article', 'date_add', 'date_upd', 'status',)
    list_filter = ('date_add', 'date_upd', 'status',)
    search_field = ('auteur')
    actions = ('active', 'desactive') 
    def active(self, request, queryset):
        queryset.update(status = True)
        self.message_user(request, 'Activer une Commentaire')
    active.short_description = 'active Commentaire'

    def desactive(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver une Commentaire')
    desactive.short_description = 'desactive Commentaire'
    ordering = ('auteur','article')
    list_per_page = 100
    date_hierarchy = ('date_add')
    list_display_links = ('auteur',)

    