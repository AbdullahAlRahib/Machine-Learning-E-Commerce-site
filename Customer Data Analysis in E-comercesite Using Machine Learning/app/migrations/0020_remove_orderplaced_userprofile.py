# Generated by Django 3.1.6 on 2022-12-15 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20221215_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='userprofile',
        ),
    ]
