# Generated by Django 4.1 on 2022-08-22 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('profession', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.DateTimeField()),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='calendarPsy.patient')),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendarPsy.professional')),
            ],
        ),
    ]
