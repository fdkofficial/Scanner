# Generated by Django 3.2.16 on 2023-05-09 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0014_unit_qr_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='sampledata',
            name='took_a_round',
            field=models.BooleanField(default=False),
        ),
    ]