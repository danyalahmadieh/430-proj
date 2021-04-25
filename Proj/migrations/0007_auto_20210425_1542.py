# Generated by Django 3.2 on 2021-04-25 12:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proj', '0006_auto_20210423_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='m_date',
            field=models.DateTimeField(default='2000-10-02'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meeting',
            name='m_endhours',
            field=models.TimeField(default=datetime.time(17, 0)),
        ),
        migrations.AddField(
            model_name='meeting',
            name='m_starthours',
            field=models.TimeField(default=datetime.time(9, 0)),
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='doctor',
        ),
        migrations.AddField(
            model_name='meeting',
            name='doctor',
            field=models.ManyToManyField(to='Proj.Doctors'),
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='patient',
        ),
        migrations.AddField(
            model_name='meeting',
            name='patient',
            field=models.ManyToManyField(to='Proj.Patients'),
        ),
    ]
