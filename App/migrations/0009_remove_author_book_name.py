# Generated by Django 3.0 on 2020-05-24 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_remove_publisher_book_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='book_name',
        ),
    ]
