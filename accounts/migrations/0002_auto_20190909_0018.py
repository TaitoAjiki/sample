# Generated by Django 2.2.4 on 2019-09-08 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=50, unique=True, verbose_name='ユーザーネーム'),
        ),
    ]