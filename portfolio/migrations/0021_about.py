# Generated by Django 4.1.7 on 2023-05-11 00:23

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_alter_comment_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=84)),
                ('img', models.ImageField(upload_to='about_img/')),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
    ]