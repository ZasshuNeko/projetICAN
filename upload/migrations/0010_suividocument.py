# Generated by Django 3.0.7 on 2020-09-29 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import upload.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('upload', '0009_auto_20200917_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuiviDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=5000)),
                ('description', models.CharField(max_length=5000)),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('fichiers', models.FileField(null=True, upload_to=upload.models.user_directory_path)),
                ('etude', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.JonctionUtilisateurEtude')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
