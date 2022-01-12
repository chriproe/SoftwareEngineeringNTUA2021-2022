# Generated by Django 4.0.1 on 2022-01-12 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('providerAbbr', models.CharField(max_length=2, unique=True)),
                ('providerName', models.CharField(max_length=50, unique=True)),
                ('iban', models.CharField(max_length=50)),
                ('bankname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicleid', models.CharField(max_length=12, unique=True)),
                ('tagid', models.CharField(max_length=9, unique=True)),
                ('licenceYear', models.IntegerField()),
                ('tagProvider', models.CharField(max_length=50)),
                ('tagProviderAbbr', models.CharField(max_length=2)),
                ('vehicle_fk1', models.ForeignKey(db_constraint=False, default='', on_delete=django.db.models.deletion.CASCADE, related_name='tagProvider', to='tl2175app.provider')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stationid', models.CharField(default='', max_length=4)),
                ('stationProvider', models.CharField(max_length=50)),
                ('stationName', models.CharField(max_length=50)),
                ('station_fk', models.ForeignKey(db_constraint=False, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='tl2175app.provider')),
            ],
        ),
        migrations.CreateModel(
            name='Passes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passid', models.CharField(max_length=20, null=True)),
                ('timestamp', models.DateTimeField()),
                ('charge', models.DecimalField(decimal_places=2, max_digits=5)),
                ('stationRef', models.CharField(max_length=50)),
                ('vehicleRef', models.CharField(max_length=12)),
                ('passes_fk1', models.ForeignKey(db_constraint=False, default='', on_delete=django.db.models.deletion.CASCADE, to='tl2175app.station')),
                ('passes_fk2', models.ForeignKey(db_constraint=False, default='', on_delete=django.db.models.deletion.CASCADE, to='tl2175app.vehicle')),
            ],
        ),
    ]
