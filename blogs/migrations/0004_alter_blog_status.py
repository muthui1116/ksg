# Generated by Django 4.2.3 on 2023-08-04 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default=0, max_length=255),
        ),
    ]
