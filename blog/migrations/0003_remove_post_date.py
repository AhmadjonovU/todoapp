# Generated by Django 3.1.13 on 2021-10-28 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
    ]
