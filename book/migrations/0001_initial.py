# Generated by Django 5.0.6 on 2024-10-01 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
