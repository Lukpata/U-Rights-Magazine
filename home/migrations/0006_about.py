# Generated by Django 4.1.1 on 2023-02-28 11:47

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_news_slug_alter_piece_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('content', tinymce.models.HTMLField()),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
    ]
