# Generated by Django 4.2.3 on 2023-08-05 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_sociallink_alter_about_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sociallink',
            name='platform',
            field=models.CharField(max_length=255),
        ),
    ]
