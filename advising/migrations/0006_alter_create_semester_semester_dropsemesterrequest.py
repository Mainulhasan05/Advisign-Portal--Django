# Generated by Django 4.0.2 on 2022-03-30 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advising', '0005_alter_assignedcourse_for_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_semester',
            name='semester',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='DropSemesterRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(default=False, max_length=255)),
                ('message', models.CharField(default=False, max_length=255)),
                ('student_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]