# Generated by Django 3.1.7 on 2021-04-09 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_date', models.CharField(max_length=50)),
                ('created', models.DateField(auto_now=True)),
                ('modified', models.DateField(auto_now_add=True)),
                ('day_or_night', models.BooleanField(default=True)),
                ('air_temperature', models.IntegerField(blank=True)),
                ('water_temperature', models.IntegerField(blank=True)),
                ('sample_latitude', models.FloatField(max_length=15)),
                ('sample_longitude', models.FloatField(max_length=15)),
                ('sample_depth', models.FloatField(blank=True, max_length=8)),
                ('is_completed', models.BooleanField(default=False)),
                ('total_zooplankton', models.IntegerField(default=0)),
                ('total_phytoplankton', models.IntegerField(default=0)),
                ('total_plastic_fibers', models.IntegerField(default=0)),
                ('total_plastic_particles', models.IntegerField(default=0)),
                ('submitted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sample_sets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WeatherCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.CharField(blank=True, choices=[('Storm', 'Stormy'), ('Rain', 'Rainy'), ('Sun', 'Sunny'), ('Cloud', 'Cloudy'), ('Snow', 'Snowy')], max_length=6)),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weather_conditions', to='sample_set.sampleset')),
            ],
        ),
        migrations.CreateModel(
            name='WaterSurface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.CharField(blank=True, choices=[('O', 'Oily surface'), ('F', 'Foamy surface'), ('B', 'Bioluminescent')], max_length=1)),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='water_surface', to='sample_set.sampleset')),
            ],
        ),
    ]