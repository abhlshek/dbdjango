# Generated by Django 5.0.6 on 2024-10-03 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_studentid'),
    ]

    operations = [
        migrations.CreateModel(
            name='coll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('classroom', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='studentid',
            name='roll',
            field=models.IntegerField(),
        ),
    ]
