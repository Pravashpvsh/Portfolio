# Generated by Django 4.2.3 on 2023-07-28 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_abouts_title_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('tittle_description', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
