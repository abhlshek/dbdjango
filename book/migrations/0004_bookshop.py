# Generated by Django 5.0.6 on 2024-10-03 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_coll_alter_studentid_roll'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=200)),
                ('subject', models.IntegerField(choices=[(1, 'C'), (2, 'Java'), (3, 'Python')], default=1)),
                ('price', models.IntegerField()),
                ('cover', models.ImageField(upload_to='static/')),
            ],
        ),
    ]
