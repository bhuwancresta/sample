# Generated by Django 2.0.6 on 2018-08-06 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0011_auto_20180806_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourteam',
            name='profile',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
