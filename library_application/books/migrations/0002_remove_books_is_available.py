# Generated by Django 2.2.2 on 2019-06-07 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='is_available',
        ),
    ]