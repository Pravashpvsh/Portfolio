# Generated by Django 4.2.3 on 2023-07-29 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abouts',
            name='is_freelance_available',
        ),
    ]
