# Generated by Django 4.2.3 on 2023-07-28 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_contact_remove_client_hero_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='display',
        ),
    ]
