# Generated by Django 4.2.5 on 2023-10-03 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='type',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.IntegerField(null=True),
        ),
    ]
