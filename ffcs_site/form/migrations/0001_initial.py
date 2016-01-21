# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Class_X', models.DecimalField(max_digits=2, decimal_places=2)),
                ('Class_XII', models.DecimalField(max_digits=2, decimal_places=2)),
                ('UG', models.DecimalField(help_text=b'CGPA upto 1 decimal place', max_digits=2, decimal_places=2)),
                ('PG', models.DecimalField(max_digits=2, decimal_places=2)),
                ('Resume', models.FileField(help_text=b'Upload your updated resume', upload_to=b'/home/ubuntu/djcode/ffcs_site/')),
            ],
        ),
        migrations.CreateModel(
            name='ask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Project_Status', models.CharField(help_text=b'choose yes if you have already done your project', max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')])),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('First_Name', models.CharField(max_length=30)),
                ('Middle_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('Registration_ID', models.CharField(help_text=b'Your College ID', unique=True, max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title_Of_Project', models.TextField()),
                ('Abstract', models.TextField()),
                ('Keywords', models.TextField(help_text=b'Keywords related to your peoject separated by comma')),
            ],
        ),
        migrations.CreateModel(
            name='TopicOfInterest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Topics', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='Interest',
            field=models.ManyToManyField(to='form.TopicOfInterest'),
        ),
    ]
