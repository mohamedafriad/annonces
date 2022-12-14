# Generated by Django 3.2.16 on 2022-10-09 14:57

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
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=300, verbose_name='Nom Région(ar)')),
                ('nom_fr', models.CharField(blank=True, max_length=300, null=True, verbose_name='Nom Région(fr)')),
            ],
            options={
                'verbose_name': 'Région',
                'verbose_name_plural': 'Régions',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=300, verbose_name='Nom Province(ar)')),
                ('nom_fr', models.CharField(blank=True, max_length=300, null=True, verbose_name='Nom Province(fr)')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provinces', to='structure.region', verbose_name='Région')),
            ],
            options={
                'verbose_name': 'Province',
                'verbose_name_plural': 'Provinces',
            },
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='membres', to='structure.province')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='membres', to='structure.region')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Membre',
                'verbose_name_plural': 'Membres',
            },
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=300, verbose_name='Nom Commune(ar)')),
                ('nom_fr', models.CharField(blank=True, max_length=300, null=True, verbose_name='Nom Commune(fr)')),
                ('milieu', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Urbain'), (2, 'Rural')], default=2, null=True, verbose_name='Milieu')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communes', to='structure.province', verbose_name='Province')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communes', to='structure.region', verbose_name='Région')),
            ],
            options={
                'verbose_name': 'Commune',
                'verbose_name_plural': 'Communes',
            },
        ),
    ]
