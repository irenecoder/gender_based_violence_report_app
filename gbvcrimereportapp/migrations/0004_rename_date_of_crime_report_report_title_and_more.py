# Generated by Django 4.0.3 on 2022-03-25 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gbvcrimereportapp', '0003_rename_reportedcrimes_report_alter_report_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='date_of_crime',
            new_name='report_title',
        ),
        migrations.AddField(
            model_name='report',
            name='reporter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='crime_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
