# Generated by Django 2.2.5 on 2019-10-23 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('reference', models.URLField(verbose_name='Link for Reference')),
                ('level', models.CharField(choices=[('cantrip', 'Cantrip'), ('1', '1st'), ('2', '2nd'), ('3', '3rd'), ('4', '4th'), ('5', '5th'), ('6', '6th'), ('7', '7th'), ('8', '8th'), ('9', '9th')], default='cantrip', max_length=100)),
                ('sht', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='sheets.Sheet')),
            ],
        ),
    ]
