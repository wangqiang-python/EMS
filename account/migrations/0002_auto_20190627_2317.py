# Generated by Django 2.0.6 on 2019-06-27 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=20),
        ),
    ]
