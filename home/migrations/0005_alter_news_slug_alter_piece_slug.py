# Generated by Django 4.1.1 on 2023-02-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='piece',
            name='slug',
            field=models.SlugField(),
        ),
    ]
