# Generated by Django 5.0.6 on 2024-06-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('idCourse', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nameCourse', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]