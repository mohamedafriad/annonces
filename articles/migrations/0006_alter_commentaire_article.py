# Generated by Django 4.1.1 on 2022-10-18 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_commentaire_auteur_alter_commentaire_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='articles.article', verbose_name='Article'),
        ),
    ]