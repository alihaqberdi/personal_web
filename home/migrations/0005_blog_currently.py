# Generated by Django 4.1.7 on 2023-03-10 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_blog_frilance'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='currently',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
