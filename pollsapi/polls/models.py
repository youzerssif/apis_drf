from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.

class Utilisateur(models.Model):
    """Model definition for Utilisateur."""
    GENRE = [
        ('F', 'Femme'),
        ('M', 'Homme'),

    ]
    # TODO: Define fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='auteur')
    photo_profile = models.ImageField(upload_to='photo', null='True')
    adresse = models.CharField(max_length=255)
    genre = models.CharField(max_length=255, choices=GENRE)
    contact = models.CharField(max_length=255)

    slug = models.SlugField(unique=True, null=True, blank=True)

    status = models.BooleanField(default=True, blank=True, null=True)
    date_add = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_upd = models.DateTimeField(auto_now=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.user.username)))
        super(Utilisateur, self).save(*args, **kwargs)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Utilisateur."""

        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

    def __str__(self):
        """Unicode representation of Utilisateur."""
        return self.user.first_name


class Categorie(models.Model):
    """Model definition for Categorie."""

    # TODO: Define fields here
    nom = models.CharField(max_length=255, null=True)
    
    status = models.BooleanField(default=True, blank=True, null=True)
    date_add = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_upd = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.nom


class Article(models.Model):
    """Model definition for Article."""

    # TODO: Define fields here
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="categoriearticle")
    titre = models.CharField(max_length=255, null=True,)
    image = models.FileField(upload_to='image_article', null=True)
    description = models.TextField()
    
    status = models.BooleanField(default=True, blank=True, null=True)
    date_add = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_upd = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.titre


class Commentaire(models.Model):
    """Model definition for Commentaire."""

    # TODO: Define fields here
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="commentaire_auteur")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="commentaire_article")
    message = models.TextField()
    
    status = models.BooleanField(default=True, blank=True, null=True)
    date_add = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_upd = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        """Meta definition for Commentaire."""

        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        """Unicode representation of Commentaire."""
        return self.auteur
