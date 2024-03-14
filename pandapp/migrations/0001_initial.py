# Generated by Django 4.2.11 on 2024-03-12 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelephoneNumberCatalogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odt_file', models.FileField(upload_to='ods/')),
            ],
        ),
        migrations.CreateModel(
            name='TelephoneNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('telephone_number', models.PositiveBigIntegerField()),
            ],
        ),
    ]
