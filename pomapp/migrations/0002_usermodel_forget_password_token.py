# Generated by Django 4.1.5 on 2023-01-20 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='forget_password_token',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
