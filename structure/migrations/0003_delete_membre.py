# Generated by Django 4.1.1 on 2022-10-13 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0002_alter_commune_id_alter_membre_id_alter_province_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Membre',
        ),
    ]
