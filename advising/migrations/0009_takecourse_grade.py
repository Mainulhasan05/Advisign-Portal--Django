# Generated by Django 3.2.5 on 2022-04-10 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advising', '0008_takecourse_withdraw_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='takecourse',
            name='grade',
            field=models.CharField(blank=True, default='Did not assign', max_length=10, null=True),
        ),
    ]