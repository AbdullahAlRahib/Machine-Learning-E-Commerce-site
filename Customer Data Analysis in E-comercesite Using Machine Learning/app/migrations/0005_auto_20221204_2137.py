# Generated by Django 3.1.6 on 2022-12-04 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20221204_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('F', 'Fashion'), ('G', 'Grocery'), ('LA', 'Laptop & Accessory'), ('MA', 'Mobile & Accessory'), ('MP', 'Mobile Phone'), ('OT', 'Others')], max_length=2),
        ),
    ]
