# Generated by Django 2.1.4 on 2019-01-14 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyStarbucks', '0002_auto_20190106_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail_drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('image', models.CharField(max_length=255)),
                ('price', models.FloatField()),
            ],
        ),
    ]
