# Generated by Django 4.2.3 on 2023-07-29 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_resume_alter_project_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='education',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='professional_experience',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
