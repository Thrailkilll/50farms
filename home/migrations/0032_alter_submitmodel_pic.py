# Generated by Django 3.2.5 on 2021-08-24 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_auto_20210709_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitmodel',
            name='pic',
            field=models.ImageField(null=True, upload_to=None),
        ),
    ]