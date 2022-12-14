# Generated by Django 4.1.1 on 2022-10-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=500, verbose_name='Titre')),
                ('auteur', models.CharField(blank=True, max_length=500, null=True, verbose_name='Auteur')),
                ('journal', models.CharField(blank=True, max_length=250, null=True, verbose_name='Journal')),
                ('date_creation', models.DateField(blank=True, null=True, verbose_name='Date Création')),
                ('date_publication', models.DateField(blank=True, null=True, verbose_name='Date Publication')),
                ('contenu', models.CharField(max_length=5000, verbose_name='Contenu')),
                ('tags', models.CharField(blank=True, max_length=250, verbose_name='Mots clés')),
                ('image', models.URLField(blank=True, null=True, verbose_name='Affiche')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Lien')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
