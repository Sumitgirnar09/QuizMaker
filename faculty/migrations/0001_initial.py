# Generated by Django 4.0.3 on 2022-10-28 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('Teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default=0, max_length=50)),
                ('Dept', models.CharField(default='', max_length=70)),
                ('Dob', models.DateField(default=datetime.datetime.now)),
                ('pass1', models.CharField(default='', max_length=70)),
                ('pass2', models.CharField(default='', max_length=70)),
                ('email', models.EmailField(default='', max_length=100)),
            ],
        ),
    ]
