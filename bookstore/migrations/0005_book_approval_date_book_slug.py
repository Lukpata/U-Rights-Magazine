# Generated by Django 4.1.1 on 2023-03-08 15:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_alter_book_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='approval_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default='shddhhdn'),
        ),
    ]
