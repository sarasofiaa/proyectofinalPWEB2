# Generated by Django 5.0.6 on 2024-06-12 01:35

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_section_section_unique_workload'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('idEvent', models.AutoField(primary_key=True, serialize=False)),
                ('amountEvent', models.IntegerField()),
                ('percentageProgress', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('percentageExam', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('idCourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
            ],
        ),
    ]
