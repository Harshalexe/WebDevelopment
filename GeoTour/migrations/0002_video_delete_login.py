# Generated by Django 4.1.4 on 2022-12-23 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeoTour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='video/%y')),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]