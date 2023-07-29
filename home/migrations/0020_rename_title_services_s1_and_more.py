# Generated by Django 4.2.3 on 2023-07-29 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_sdescription_remove_services_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='title',
            new_name='s1',
        ),
        migrations.RemoveField(
            model_name='services',
            name='title_description',
        ),
        migrations.AddField(
            model_name='services',
            name='s1d',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='s2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='s2d',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='s3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='s3d',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='s4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='s4d',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='s5',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='s5d',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='s6',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='s6d',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
