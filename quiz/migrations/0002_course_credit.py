# Generated by Django 4.0.3 on 2022-11-03 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Credit',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
