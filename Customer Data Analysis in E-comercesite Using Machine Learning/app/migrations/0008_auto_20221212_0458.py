# Generated by Django 3.1.6 on 2022-12-12 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_auto_20221205_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Dhaka', 'Dhaka'), ('Mymensingh', 'Mymensingh'), ('Chitaguang', 'Chitaguang'), ('Barishal', 'Barishal'), ('Commila', 'Commila'), ('Sylhet', 'Sylhet'), ('Coxs Bazer', 'Coxs Bazer'), ('Tangail', 'Tangail')], max_length=50),
        ),
        migrations.CreateModel(
            name='DataTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
