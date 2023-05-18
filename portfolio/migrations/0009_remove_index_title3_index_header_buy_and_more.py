# Generated by Django 4.1.7 on 2023-05-07 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_category_portfolio_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index',
            name='title3',
        ),
        migrations.AddField(
            model_name='index',
            name='header_buy',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='index',
            name='header_buy_hover',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='head_img',
            field=models.ImageField(blank=True, null=True, upload_to='head_img'),
        ),
        migrations.AlterField(
            model_name='index',
            name='portfolio_h3',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='title1',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='title2',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='title_discription',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='title_footer',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='title_footer_hover',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='title_footer_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
