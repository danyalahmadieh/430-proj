# Generated by Django 3.2 on 2021-04-23 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Proj', '0005_auto_20210415_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='p_history',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.CharField(default='', max_length=30)),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]