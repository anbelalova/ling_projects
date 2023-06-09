# Generated by Django 4.1.2 on 2022-10-30 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectsearch',
            options={'verbose_name': 'БД проекта', 'verbose_name_plural': 'БД проектов'},
        ),
        migrations.AlterField(
            model_name='searchobjects',
            name='frame',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.secondlevelframes'),
        ),
    ]
