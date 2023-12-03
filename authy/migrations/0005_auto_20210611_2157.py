# Generated by Django 3.2.3 on 2021-06-11 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0004_auto_20210611_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='select',
            field=models.CharField(blank=True, choices=[('Basic', 'Basic'), ('Standard', 'Standard'), ('Premium', 'Premium')], max_length=8, null=True, verbose_name='Package'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='url',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]