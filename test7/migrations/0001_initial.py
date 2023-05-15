# Generated by Django 4.1.7 on 2023-02-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
