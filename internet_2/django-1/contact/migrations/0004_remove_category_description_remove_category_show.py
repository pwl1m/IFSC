# Generated by Django 5.0 on 2023-12-09 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_category_contact_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='show',
        ),
    ]
