# Generated by Django 2.1.7 on 2019-08-17 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'g_donate'), (2, 'r_donate')], null=True),
        ),
    ]
