# Generated by Django 2.1.4 on 2019-01-06 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyStarbucks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestbook',
            name='content',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='guestbook',
            name='title',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
