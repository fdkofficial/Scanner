# Generated by Django 3.2.16 on 2023-05-09 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0013_alter_unit_unit_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='qr_image',
            field=models.ImageField(blank=True, null=True, upload_to='QRCode'),
        ),
    ]