# Generated by Django 4.2.3 on 2023-07-28 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_socialplatform_github_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='cSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(blank=True, max_length=50, null=True)),
                ('cpercentage', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
