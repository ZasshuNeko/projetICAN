# Generated by Django 3.0.7 on 2020-09-17 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('upload', '0005_auto_20200831_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suiviupload',
            name='controle_qualite',
        ),
        migrations.CreateModel(
            name='DossierUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date de création')),
                ('controle_qualite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='upload.RefControleQualite')),
                ('upload', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='upload.SuiviUpload')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='jonctionetapesuivi',
            name='upload',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='upload.DossierUpload'),
        ),
    ]
