# Generated by Django 4.2.3 on 2023-07-29 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_remove_abouts_is_freelance_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('summary', models.TextField(blank=True, max_length=255, null=True)),
                ('education', models.TextField(blank=True, max_length=255, null=True)),
                ('professional_experience', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
