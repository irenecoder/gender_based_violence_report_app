# Generated by Django 4.0.3 on 2022-03-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gbvcrimereportapp', '0004_rename_date_of_crime_report_report_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='phone_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]