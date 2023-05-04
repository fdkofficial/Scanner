# Generated by Django 3.2.16 on 2023-05-04 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scanner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laberatory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_no', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SampleData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collect_date', models.DateTimeField(auto_now=True)),
                ('drop_of_date', models.DateTimeField()),
                ('reciever_id', models.CharField(max_length=1000)),
                ('collector_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('destination', models.ManyToManyField(null=True, to='scanner.Laberatory')),
                ('origin', models.ManyToManyField(null=True, to='scanner.Department')),
                ('sample_no', models.ManyToManyField(null=True, to='scanner.Sample')),
            ],
        ),
        migrations.DeleteModel(
            name='Building',
        ),
        migrations.DeleteModel(
            name='Samples',
        ),
    ]
