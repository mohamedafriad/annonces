# Generated by Django 4.1.1 on 2022-11-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonce', '0002_alter_annonce_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='entreprise',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/% Y/% m/% d/'),
        ),
    ]