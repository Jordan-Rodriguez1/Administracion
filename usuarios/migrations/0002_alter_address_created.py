# Generated by Django 4.2.7 on 2023-11-13 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
