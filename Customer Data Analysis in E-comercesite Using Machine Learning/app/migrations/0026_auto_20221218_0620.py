# Generated by Django 3.1.6 on 2022-12-18 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20221218_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='userprofile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userprofile'),
        ),
    ]
