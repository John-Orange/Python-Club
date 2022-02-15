# Generated by Django 4.0.2 on 2022-02-04 22:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetingtitle', models.CharField(max_length=225)),
                ('meetingdate', models.DateField()),
                ('meetingtime', models.TimeField()),
                ('meetinglocation', models.TextField(blank=True, null=True)),
                ('meetingagenda', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Meeting',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourcename', models.CharField(max_length=225)),
                ('resourcetype', models.CharField(max_length=225)),
                ('resourceURL', models.URLField()),
                ('enterdate', models.DateField()),
                ('resourcedescrip', models.TextField(blank=True, null=True)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Resource',
            },
        ),
        migrations.CreateModel(
            name='MeetingMinutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutestext', models.TextField(blank=True, null=True)),
                ('attendance', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('meetingID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='club.meeting')),
            ],
            options={
                'db_table': 'MeetingMinutes',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventtitle', models.CharField(max_length=225)),
                ('eventlocation', models.CharField(max_length=225)),
                ('eventdate', models.DateField()),
                ('eventtime', models.TimeField()),
                ('eventdescrip', models.TextField(blank=True, null=True)),
                ('userIDmember', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Event',
            },
        ),
    ]