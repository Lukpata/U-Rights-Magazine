# Generated by Django 4.1.1 on 2023-03-04 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noise', '0004_alter_poem_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='cover_anotation',
            field=models.CharField(default='Joseph Mills', max_length=200),
        ),
    ]