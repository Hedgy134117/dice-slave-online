# Generated by Django 2.2.5 on 2020-04-02 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0004_auto_20191219_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='acrobatics',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sheet',
            name='animalHandling',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sheet',
            name='arcana',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sheet',
            name='athletics',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sheet',
            name='deception',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sheet',
            name='history',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sheet',
            name='insight',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sheet',
            name='intimidation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sheet',
            name='investigation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sheet',
            name='medicine',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sheet',
            name='nature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sheet',
            name='perception',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sheet',
            name='performance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sheet',
            name='persuasion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sheet',
            name='religion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sheet',
            name='sleightOfHand',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sheet',
            name='stealth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sheet',
            name='survival',
            field=models.BooleanField(default=False),
        ),
    ]