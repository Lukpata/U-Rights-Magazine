# Generated by Django 4.1.1 on 2023-02-28 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_news_piece_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default='news'),
        ),
    ]
