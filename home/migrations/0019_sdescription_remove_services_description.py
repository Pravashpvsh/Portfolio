# Generated by Django 4.2.3 on 2023-07-29 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_cskill'),
    ]

    operations = [
        migrations.CreateModel(
            name='sdescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='services',
            name='description',
        ),
    ]
