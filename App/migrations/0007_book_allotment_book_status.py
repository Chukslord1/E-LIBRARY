# Generated by Django 3.0 on 2020-05-24 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20200524_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_allotment',
            name='book_status',
            field=models.TextField(blank=True, null=True),
        ),
    ]