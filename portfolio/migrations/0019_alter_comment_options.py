# Generated by Django 4.1.7 on 2023-05-10 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_alter_comment_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',)},
        ),
    ]