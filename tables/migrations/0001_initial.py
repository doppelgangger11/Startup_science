# Generated by Django 4.1.7 on 2023-10-19 12:51

import datetime
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
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
                ('patent', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Table23',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('name_of_partner', models.CharField(max_length=100)),
                ('date_of_contract', models.DateField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('availability', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Table26',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.CharField(max_length=100)),
                ('subject_of_contract', models.CharField(max_length=100)),
                ('directon_of_speciality', models.CharField(max_length=40)),
                ('date_of_conclusion_of_the_contract', models.DateField()),
                ('terms_of_the_contract', models.CharField(max_length=40)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='TeachersAddInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('degree', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]