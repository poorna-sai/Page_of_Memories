# Generated by Django 4.1.5 on 2023-01-23 15:59

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomapp', '0003_alter_usermodel_forget_password_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateDairy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
