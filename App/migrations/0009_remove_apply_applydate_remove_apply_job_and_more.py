# Generated by Django 4.2.5 on 2023-10-04 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_apply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='applydate',
        ),
        migrations.RemoveField(
            model_name='apply',
            name='job',
        ),
        migrations.RemoveField(
            model_name='apply',
            name='seeker',
        ),
        migrations.AddField(
            model_name='apply',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='apply',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='apply',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
