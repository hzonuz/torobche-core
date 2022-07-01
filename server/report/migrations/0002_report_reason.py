# Generated by Django 4.0.5 on 2022-07-01 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='reason',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'WRONG_PRICE'), (2, 'WRONG_DESCRIPTION'), (3, 'WRONG_CATEGORY'), (4, 'WRONG_URL'), (5, 'WRONG_SHOP'), (6, 'WRONG_DETAIL'), (7, 'OTHER'), (8, 'UNKNOWN')], null=True),
        ),
    ]
