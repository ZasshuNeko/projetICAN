# Generated by Django 3.0.7 on 2020-08-21 08:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RefControleQualite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=5000)),
            ],
            options={
                'db_table': 'upload_refcontrolequalite',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RefEtudes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=5000)),
                ('date_ouverture', models.DateTimeField("Date d'ouverture")),
            ],
            options={
                'db_table': 'upload_refetudes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RefEtatEtape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=5000)),
            ],
            options={
                'db_table': 'upload_refetatetape',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SuiviUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
                ('etude', models.ForeignKey("JonctionUtilisateurEtude", on_delete=models.CASCADE)),
                ('id_patient', models.CharField(max_length=5000)),
                ('date_upload', models.DateTimeField("Date d'envois")),
                ('date_examen', models.DateTimeField("Date examen")),
                ('controle_qualite', models.ForeignKey("RefControleQualite", on_delete=models.CASCADE)),
            ],
            options={
                'db_table': 'upload_suiviupload',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='JonctionUtilisateurEtude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user',models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
                ('etude', models.ForeignKey('RefEtudes', on_delete=models.CASCADE)),
                ('date_autorisation', models.DateTimeField("Date d'autorisation")),
            ],
            options={
                'db_table': 'upload_jonctionutilisateuretude',
                'managed': True,
            },
        ),

        migrations.CreateModel(
            name='RefInfocentre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=5000)),
                ('numero', models.FloatField()),
                ('date_ajout', models.DateTimeField("Date d'ajout")),
                ('user', models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
            options={
                'db_table': 'upload_refinfocentre',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RefEtapeEtude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=5000)),
                ('etude', models.ForeignKey("RefEtudes", on_delete=models.CASCADE)),
            ],
            options={
                'db_table': 'upload_refetapeetude',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='JonctionEtapeSuivi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ForeignKey("SuiviUpload", on_delete=models.CASCADE)),
                ('etape', models.ForeignKey("RefEtapeEtude", on_delete=models.CASCADE)),
                ('etat', models.ForeignKey("RefEtatEtape", on_delete=models.CASCADE)),
                ('date', models.DateTimeField("Date de l'étape")),
            ],
            options={
                'db_table': 'upload_jonctionetapesuivi',
                'managed': True,
            },

        ),
    ]
