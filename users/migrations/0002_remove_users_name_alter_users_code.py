# Generated by Django 4.2.9 on 2024-02-03 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='name',
        ),
        migrations.AlterField(
            model_name='users',
            name='code',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
