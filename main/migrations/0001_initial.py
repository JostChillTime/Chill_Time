# Generated by Django 4.2.7 on 2023-11-18 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Credits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('link', models.TextField(max_length=500)),
                ('position', models.CharField(max_length=500)),
                ('box_img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='DailyQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150)),
                ('day', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('feedback_text', models.TextField(max_length=255)),
                ('feedback_img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='InformationBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('main_text', models.TextField(max_length=500)),
                ('box_img', models.ImageField(upload_to='')),
                ('side', models.CharField(default='left', max_length=10)),
            ],
        ),
    ]