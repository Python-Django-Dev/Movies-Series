# Generated by Django 5.1.3 on 2024-12-19 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_animation_film_series_remove_login_movie_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Animation',
        ),
        migrations.DeleteModel(
            name='series',
        ),
        migrations.AlterModelOptions(
            name='film',
            options={'verbose_name': 'Movie'},
        ),
    ]
