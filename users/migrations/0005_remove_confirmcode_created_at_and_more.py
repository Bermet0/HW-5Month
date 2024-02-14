# Generated by Django 4.2.9 on 2024-02-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_confirmcode_updated_at_alter_confirmcode_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirmcode',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='confirmcode',
            name='user',
        ),
        migrations.AlterField(
            model_name='confirmcode',
            name='code',
            field=models.IntegerField(max_length=6),
        ),
    ]