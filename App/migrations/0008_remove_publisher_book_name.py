# Generated by Django 3.0 on 2020-05-24 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_book_allotment_book_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='book_name',
        ),
    ]