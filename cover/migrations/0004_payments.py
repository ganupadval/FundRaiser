# Generated by Django 4.0.3 on 2022-04-24 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover', '0003_delete_payments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.IntegerField()),
            ],
        ),
    ]