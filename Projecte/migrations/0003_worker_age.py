# Generated by Django 4.0.3 on 2022-03-21 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projecte', '0002_worker'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
