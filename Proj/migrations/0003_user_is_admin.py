# Generated by Django 3.2 on 2021-04-14 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proj', '0002_auto_20210414_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
