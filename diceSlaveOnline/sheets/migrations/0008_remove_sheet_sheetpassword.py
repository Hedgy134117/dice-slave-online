# Generated by Django 2.1 on 2019-09-25 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0007_auto_20190925_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sheet',
            name='sheetPassword',
        ),
    ]
