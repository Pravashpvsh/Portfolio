# Generated by Django 4.2.3 on 2023-07-28 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_abouts_title_description_alter_abouts_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abouts',
            name='title_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
