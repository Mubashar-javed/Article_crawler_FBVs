# Generated by Django 2.2.5 on 2020-02-05 11:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0010_delete_downloadhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='searched',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
