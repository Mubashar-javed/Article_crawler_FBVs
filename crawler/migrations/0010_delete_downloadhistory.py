# Generated by Django 2.2.5 on 2020-02-04 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0009_downloadhistory_article_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DownloadHistory',
        ),
    ]