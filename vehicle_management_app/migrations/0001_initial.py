# Generated by Django 3.2.16 on 2022-10-26 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
                ('type', models.IntegerField()),
                ('model', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
