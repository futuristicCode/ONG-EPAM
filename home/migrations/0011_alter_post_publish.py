# Generated by Django 4.0.3 on 2022-03-28 16:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_membres_photo_membres_upload_to_partenaire_upload_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 28, 16, 2, 37, 146282, tzinfo=utc)),
        ),
    ]
