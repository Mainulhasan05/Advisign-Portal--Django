# Generated by Django 3.2.5 on 2022-03-23 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advising', '0003_alter_department_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignedcourse',
            name='slug',
            field=models.SlugField(default='', max_length=255, unique=True),
        ),
    ]
