# Generated by Django 5.1.2 on 2024-11-25 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_login_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
