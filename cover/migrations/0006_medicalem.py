# Generated by Django 4.0.3 on 2022-04-25 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover', '0005_alter_payments_ammount'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalEm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('info', models.TextField()),
                ('fund_req', models.IntegerField()),
                ('fund_raised', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
