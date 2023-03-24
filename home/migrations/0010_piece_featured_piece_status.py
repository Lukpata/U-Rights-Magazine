# Generated by Django 4.1.1 on 2023-03-01 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_piece_category_alter_piece_issue_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='piece',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default='Published', max_length=200),
        ),
    ]
