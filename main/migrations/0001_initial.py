# Generated by Django 3.1.6 on 2021-02-15 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('director', models.CharField(max_length=300)),
                ('cast', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=5000)),
                ('release_date', models.DateField()),
                ('averaRating', models.FloatField()),
            ],
        ),
    ]