# Generated by Django 3.1.4 on 2020-12-03 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=250)),
            ],
        ),
    ]
