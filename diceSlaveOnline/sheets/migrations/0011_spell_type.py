# Generated by Django 2.2.5 on 2020-04-08 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0010_item_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='spell',
            name='Type',
            field=models.CharField(choices=[('offensive', 'Offensive'), ('normal', 'Normal')], default='noramal', max_length=100),
        ),
    ]