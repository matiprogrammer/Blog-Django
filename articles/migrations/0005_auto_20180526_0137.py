# Generated by Django 2.0.5 on 2018-05-25 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20180526_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.FileField(blank=True, default=None, null=True, upload_to='images', verbose_name='Obrazy'),
        ),
    ]
