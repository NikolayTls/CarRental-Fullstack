# Generated by Django 3.2.5 on 2021-10-17 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('model_year', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, null=True)),
                ('price_per_day', models.FloatField(max_length=10, null=True)),
                ('occupant_amount', models.CharField(max_length=100, null=True)),
                ('baggage_amount', models.CharField(max_length=100, null=True)),
                ('driver_age', models.FloatField(max_length=10, null=True)),
                ('Power', models.FloatField(max_length=10, null=True)),
                ('door_amount', models.FloatField(max_length=10, null=True)),
                ('acriss_code', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.city')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_date', models.DateTimeField(null=True)),
                ('dropoff_date', models.DateTimeField(null=True)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.car')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickup_city', to='accounts.city')),
                ('city1', models.ForeignKey(default='---------', on_delete=django.db.models.deletion.CASCADE, related_name='return_city', to='accounts.city')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickup_station', to='accounts.station')),
                ('station1', models.ForeignKey(default='---------', on_delete=django.db.models.deletion.CASCADE, related_name='return_station', to='accounts.station')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.category'),
        ),
    ]
