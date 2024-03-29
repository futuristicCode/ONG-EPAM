# Generated by Django 4.0.3 on 2022-03-28 14:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_alter_post_image_alter_post_publish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partenaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='uploads')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 28, 14, 43, 14, 344936, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Membres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=200)),
                ('nom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membre', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
