# Generated by Django 4.1.1 on 2023-03-10 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0006_alter_book_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-approval_date']},
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('no_of_copies', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=200)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('treated', 'treated')], default='treated', max_length=200)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.book')),
            ],
            options={
                'verbose_name': 'Book Order',
                'ordering': ['-order_date'],
            },
        ),
    ]