# Generated by Django 3.1.6 on 2022-12-15 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20221215_1814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='userprofileid',
            new_name='userprofile',
        ),
    ]
