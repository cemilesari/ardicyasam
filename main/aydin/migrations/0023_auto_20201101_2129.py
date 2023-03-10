# Generated by Django 3.0.10 on 2020-11-01 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aydin', '0022_auto_20201101_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Categori İsmi')),
            ],
            options={
                'verbose_name': 'EN Ürünler Alt Categori',
                'verbose_name_plural': 'EN Ürünler Alt Categori ',
                'ordering': ('-created',),
            },
        ),
        migrations.RemoveField(
            model_name='products',
            name='al_body',
        ),
        migrations.RemoveField(
            model_name='products',
            name='al_body2',
        ),
        migrations.RemoveField(
            model_name='products',
            name='al_body3',
        ),
        migrations.RemoveField(
            model_name='products',
            name='al_body4',
        ),
        migrations.RemoveField(
            model_name='products',
            name='al_body5',
        ),
        migrations.RemoveField(
            model_name='products',
            name='brosur',
        ),
        migrations.RemoveField(
            model_name='products',
            name='certifica',
        ),
        migrations.RemoveField(
            model_name='products',
            name='kullanim',
        ),
        migrations.AddField(
            model_name='products',
            name='dowloads',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aydin.KlavuzEN', verbose_name='Dökümanlar'),
        ),
        migrations.AddField(
            model_name='products',
            name='kod',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Ürün Kodu'),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('DIŞ ORTAM', 'DIŞ ORTAM'), ('İÇ ORTAM', 'İÇ ORTAM'), ('YARDIMCI ÜRÜNLER', 'YARDIMCI ÜRÜNLER')], default='DIŞ ORTAM', max_length=500, verbose_name='Kategori Seçiniz'),
        ),
        migrations.AddField(
            model_name='products',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aydin.ProductCategory', verbose_name='Alt Kategori'),
        ),
    ]
