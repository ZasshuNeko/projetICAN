# Generated by Django 3.0.7 on 2020-09-17 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0007_auto_20200917_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dossierupload',
            name='upload',
        ),
        migrations.AddField(
            model_name='suiviupload',
            name='dossier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='upload.DossierUpload'),
        ),
    ]
