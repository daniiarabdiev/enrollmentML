# Generated by Django 2.2.6 on 2019-10-08 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0002_auto_20191008_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportantFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200, unique=True)),
                ('imp_feat', models.FileField(upload_to='important_features/')),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200, unique=True)),
                ('weight', models.FileField(upload_to='weights/')),
            ],
        ),
    ]