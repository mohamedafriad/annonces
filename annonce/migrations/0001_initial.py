# Generated by Django 4.1.1 on 2022-10-13 21:31

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
            name='Entreprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination', models.CharField(max_length=500, verbose_name='Dénomination')),
                ('raison_soc', models.CharField(max_length=500, verbose_name='Raison sociale')),
                ('statut', models.CharField(blank=True, max_length=50, verbose_name='Statut juridique')),
                ('rc', models.CharField(blank=True, max_length=50, verbose_name='N° de RC')),
                ('ice', models.CharField(blank=True, max_length=50, verbose_name='N° de ICE')),
                ('activite', models.CharField(blank=True, max_length=500, verbose_name='Activité')),
                ('forme', models.PositiveSmallIntegerField(choices=[(1, 'Personne physique'), (2, 'Auto-entrepreneur'), (3, 'SARL'), (4, 'SARLAU'), (5, 'SNC'), (6, 'SCS'), (7, 'SCA'), (8, 'Société Annonyme Simplifiée (SAS)'), (9, 'Société Annonyme (SA)'), (10, "Groupement d'Intérêt Economique (GIE)")], default=1, verbose_name='Forme juridique')),
                ('date_immatriculation', models.DateField(blank=True, null=True, verbose_name="Date d'immatriculation")),
                ('capital', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Capital (en MAD)')),
                ('tribunal', models.CharField(blank=True, max_length=250, verbose_name='Tribunal')),
                ('ville', models.CharField(blank=True, max_length=250, verbose_name='Ville')),
                ('adresse', models.CharField(blank=True, max_length=500, verbose_name='Adresse')),
                ('longitude', models.CharField(blank=True, max_length=50, verbose_name='longitude')),
                ('latitude', models.CharField(blank=True, max_length=50, verbose_name='latitude')),
                ('fixe', models.CharField(blank=True, max_length=50, verbose_name='Fixe')),
                ('fax', models.CharField(blank=True, max_length=50, verbose_name='Fax')),
                ('email', models.CharField(blank=True, max_length=50, verbose_name='Email')),
                ('representant', models.CharField(blank=True, max_length=250, verbose_name='Représentant')),
                ('gerant', models.CharField(blank=True, max_length=250, verbose_name='Gérant')),
            ],
            options={
                'verbose_name': 'Entreprise',
                'verbose_name_plural': 'Entreprises',
            },
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_inscription', models.DateField(blank=True, null=True, verbose_name='Date inscription')),
                ('entreprise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='annonce.entreprise')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profil',
                'verbose_name_plural': 'Profils',
            },
        ),
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=200, verbose_name='Référence')),
                ('intitule', models.CharField(max_length=250, verbose_name='Intitule')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Date création')),
                ('date_publication', models.DateField(blank=True, null=True, verbose_name='Date publication')),
                ('contenu', models.CharField(max_length=1000, verbose_name='Contenu')),
                ('etat', models.PositiveSmallIntegerField(choices=[(1, 'En attente'), (2, 'Publiée'), (3, 'Rejetée')], default=1, verbose_name='Etat')),
                ('categorie', models.PositiveSmallIntegerField(choices=[(1, 'Constitution'), (2, "Cessation d'activité"), (3, 'Modification de société')], default=1, verbose_name='Catégorie')),
                ('type_annonce', models.PositiveSmallIntegerField(choices=[(1, 'Constitution'), (2, 'Dissolution'), (3, 'Clôture de la liquidation'), (4, "Continuité de l'ativité"), (5, 'Changement de dirigeant'), (6, 'Transfert de siège social'), (7, "Changement d'objet social"), (8, 'Changement de dénomination'), (9, 'Tranformation de la forme sociale'), (10, 'Cession de parts sociales'), (11, 'Réduction de capital'), (12, 'Augmentation de capital')], default=1, verbose_name='Type')),
                ('annonceur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='annonces', to='annonce.profil')),
            ],
            options={
                'verbose_name': 'Annonce',
                'verbose_name_plural': 'Annonces',
            },
        ),
    ]
