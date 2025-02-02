# Generated by Django 5.0.7 on 2024-07-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(upload_to='Images')),
                ('name', models.CharField(max_length=60)),
                ('instructor', models.CharField(max_length=30)),
                ('duration', models.CharField(max_length=20)),
                ('price', models.FloatField()),
            ],
        ),
    ]
