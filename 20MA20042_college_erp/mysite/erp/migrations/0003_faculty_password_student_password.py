# Generated by Django 5.0.dev20230405040931 on 2023-04-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_alter_course_course_id_prereq'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='password',
            field=models.CharField(default='password', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='password', max_length=100),
        ),
    ]