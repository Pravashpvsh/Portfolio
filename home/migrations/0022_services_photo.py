# Generated by Django 4.2.3 on 2023-07-29 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_rename_s1_services_title_remove_services_s1d_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='services/'),
        ),
    ]
