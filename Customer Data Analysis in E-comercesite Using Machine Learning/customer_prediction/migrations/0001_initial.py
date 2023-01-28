# Generated by Django 3.1.6 on 2022-12-26 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualSpending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_sess', models.IntegerField()),
                ('avg_spend_time_app', models.IntegerField()),
                ('avg_spend_time_web', models.IntegerField()),
                ('mem_len', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_care_call', models.IntegerField()),
                ('customer_rating', models.IntegerField()),
                ('product_cost', models.IntegerField()),
                ('no_of_pur', models.IntegerField()),
                ('product_importance', models.CharField(choices=[('high', 'high'), ('medium', 'medium'), ('low', 'low')], default='high', max_length=50)),
                ('offer_discount', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
    ]
