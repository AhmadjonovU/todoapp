# Generated by Django 3.1.13 on 2021-10-28 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
    ]
