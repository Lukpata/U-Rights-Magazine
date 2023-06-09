# Generated by Django 4.1.1 on 2023-02-27 22:10

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Masthead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='editor photos')),
                ('editor_bio', tinymce.models.HTMLField()),
            ],
            options={
                'verbose_name_plural': 'Masthead',
            },
        ),
    ]
