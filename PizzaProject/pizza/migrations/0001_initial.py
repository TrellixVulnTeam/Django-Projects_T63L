# Generated by Django 3.1.4 on 2020-12-03 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_size', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_type', models.CharField(choices=[('square', 'Square'), ('regular', 'Regular')], max_length=150)),
                ('size_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.sizes')),
                ('topping_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.toppings')),
            ],
        ),
    ]
