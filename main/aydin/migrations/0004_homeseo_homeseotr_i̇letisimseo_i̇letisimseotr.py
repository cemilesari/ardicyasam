# Generated by Django 3.0.10 on 2020-10-13 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aydin', '0003_auto_20201013_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='İletisimSeoTR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('titlesite', models.CharField(blank=True, max_length=200, null=True, verbose_name='Site Title')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Meta Description')),
                ('keywords', models.ManyToManyField(blank=True, null=True, to='aydin.KeywordsTR', verbose_name='Keywords')),
            ],
            options={
                'verbose_name': 'TR SEO İletisim',
                'verbose_name_plural': 'TR SEO İletisim',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='İletisimSeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('titlesite', models.CharField(blank=True, max_length=200, null=True, verbose_name='Site Title')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Meta Description')),
                ('keywords', models.ManyToManyField(blank=True, null=True, to='aydin.Keywords', verbose_name='Keywords')),
            ],
            options={
                'verbose_name': 'EN SEO İletisim',
                'verbose_name_plural': 'EN SEO İletisim',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='HomeSeoTR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('titlesite', models.CharField(blank=True, max_length=200, null=True, verbose_name='Site Title')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Meta Description')),
                ('keywords', models.ManyToManyField(blank=True, null=True, to='aydin.KeywordsTR', verbose_name='Keywords')),
            ],
            options={
                'verbose_name': 'TR SEO Anasayfa',
                'verbose_name_plural': 'TR SEO Anasayfa',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='HomeSeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('titlesite', models.CharField(blank=True, max_length=200, null=True, verbose_name='Site Title')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Meta Description')),
                ('keywords', models.ManyToManyField(blank=True, null=True, to='aydin.Keywords', verbose_name='Keywords')),
            ],
            options={
                'verbose_name': 'EN SEOAnasayfa',
                'verbose_name_plural': 'EN SEOAnasayfa',
                'ordering': ('-created',),
            },
        ),
    ]
