# Generated by Django 5.1.3 on 2024-11-30 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_login_date_and_time_movie_date_and_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='type',
            field=models.CharField(choices=[('Action', 'Action'), ('Comedy', 'Comedy'), ('Romantic', 'Romantic'), ('Science-Fiction', 'Science-Fiction'), ('Horror', 'Horror')], max_length=40),
        ),
    ]
