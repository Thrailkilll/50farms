# Generated by Django 3.2.5 on 2021-08-24 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_alter_submitmodel_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitmodel',
            name='pic',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
