# Generated by Django 4.1.2 on 2022-10-30 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_projectsearch_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsearch',
            name='url',
            field=models.SlugField(blank=True, max_length=130, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='searchlanguages',
            name='author',
            field=models.CharField(blank=True, max_length=150, verbose_name='Сборщик данных'),
        ),
    ]
