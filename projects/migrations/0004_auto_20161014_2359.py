# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-14 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20161013_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.RemoveField(
            model_name='requestproject',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='workproject',
            name='deadline',
        ),
        migrations.AlterField(
            model_name='requestproject',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='selfproject',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workproject',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='work_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.WorkProject'),
        ),
    ]
