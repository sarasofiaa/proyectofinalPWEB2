# Generated by Django 5.0.6 on 2024-06-11 22:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_teacher_modified_alter_teacher_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('idCareer', models.AutoField(primary_key=True, serialize=False)),
                ('nameCareer', models.CharField(max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Career',
                'verbose_name_plural': 'Careers',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('idStudent', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.career')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('idRegistration', models.AutoField(primary_key=True, serialize=False)),
                ('semester', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
            options={
                'verbose_name': 'Registration',
                'verbose_name_plural': 'Registrations',
            },
        ),
    ]
