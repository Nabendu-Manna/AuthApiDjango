# Generated by Django 4.0.3 on 2022-03-19 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]