# Generated by Django 4.1.2 on 2022-10-30 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_searchobjects_construction_is'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondlevelframes',
            name='image_is',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='secondlevelframes',
            name='video_is',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
