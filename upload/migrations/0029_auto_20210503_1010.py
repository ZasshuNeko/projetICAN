# Generated by Django 3.0.7 on 2021-05-03 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0028_auto_20210427_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refetapeetude',
            name='etude',
        ),
        migrations.AddField(
            model_name='refetapeetude',
            name='etude',
            field=models.ManyToManyField(to='upload.RefEtudes'),
        ),
    ]
