# Generated by Django 4.1.3 on 2022-11-08 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.TextField(),
        ),
    ]
