# Generated by Django 3.2 on 2023-03-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aydin', '0025_auto_20230305_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='productstr',
            name='fiyat',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Fiyat'),
        ),
    ]
