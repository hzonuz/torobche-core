# Generated by Django 4.0.5 on 2022-07-01 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
