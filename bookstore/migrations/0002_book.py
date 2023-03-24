# Generated by Django 4.1.1 on 2023-03-08 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('pages', models.IntegerField()),
                ('free', models.BooleanField()),
                ('paid', models.BooleanField()),
                ('price', models.IntegerField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('excerpt', tinymce.models.HTMLField()),
                ('book_cover', models.FileField(upload_to='book covers')),
                ('status', models.CharField(choices=[('approved', 'approved'), ('pending', 'pending')], default='pending', max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]