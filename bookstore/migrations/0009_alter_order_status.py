# Generated by Django 4.1.1 on 2023-03-10 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0008_alter_order_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('treated', 'treated')], default='pending', max_length=200),
        ),
    ]
