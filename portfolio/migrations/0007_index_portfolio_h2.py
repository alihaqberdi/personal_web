# Generated by Django 4.1.7 on 2023-05-06 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_index_portfolio_h3'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='portfolio_h2',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]