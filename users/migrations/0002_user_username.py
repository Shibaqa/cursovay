# Generated by Django 5.0.7 on 2024-07-23 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
