# Generated by Django 2.1.15 on 2021-01-03 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='prodUrl',
            field=models.CharField(default='www.google.com', max_length=100),
        ),
    ]
