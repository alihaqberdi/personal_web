# Generated by Django 4.1.7 on 2023-05-10 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_portfolio_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='github_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]