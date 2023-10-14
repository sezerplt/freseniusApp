# Generated by Django 4.2.6 on 2023-10-14 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(blank=True, max_length=300, null=True)),
                ('telNumber', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startWorkDate', models.DateField(blank=True, null=True)),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreseniusApp.worktime')),
                ('user', models.ManyToManyField(to='FreseniusApp.workuser')),
            ],
        ),
    ]
