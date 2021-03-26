# Generated by Django 3.1.7 on 2021-03-26 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255, null=True)),
                ('image', models.FileField(null=True, upload_to='image_article')),
                ('description', models.TextField()),
                ('status', models.BooleanField(blank=True, default=True, null=True)),
                ('date_add', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_upd', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, null=True)),
                ('status', models.BooleanField(blank=True, default=True, null=True)),
                ('date_add', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_upd', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Categorie',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_profile', models.ImageField(null='True', upload_to='photo')),
                ('adresse', models.CharField(max_length=255)),
                ('genre', models.CharField(choices=[('F', 'Femme'), ('M', 'Homme')], max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('status', models.BooleanField(blank=True, default=True, null=True)),
                ('date_add', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_upd', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auteur', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Utilisateur',
                'verbose_name_plural': 'Utilisateurs',
            },
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('status', models.BooleanField(blank=True, default=True, null=True)),
                ('date_add', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_upd', models.DateTimeField(auto_now=True, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaire_article', to='polls.article')),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaire_auteur', to='polls.utilisateur')),
            ],
            options={
                'verbose_name': 'Commentaire',
                'verbose_name_plural': 'Commentaires',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoriearticle', to='polls.categorie'),
        ),
    ]
