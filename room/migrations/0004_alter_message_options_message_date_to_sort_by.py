# Generated by Django 4.1.3 on 2022-11-09 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_alter_message_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('date_to_sort_by',)},
        ),
        migrations.AddField(
            model_name='message',
            name='date_to_sort_by',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
