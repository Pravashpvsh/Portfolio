# Generated by Django 4.2.3 on 2023-07-26 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_hero_hero_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('hero_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('happyclient', models.IntegerField(blank=True, null=True)),
                ('project', models.IntegerField(blank=True, null=True)),
                ('awards', models.IntegerField(blank=True, null=True)),
                ('hoursupport', models.IntegerField(blank=True, null=True)),
                ('display', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Facts',
        ),
    ]