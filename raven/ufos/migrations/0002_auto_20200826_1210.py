# Generated by Django 3.1 on 2020-08-26 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ufos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='last_update',
        ),
        migrations.AddField(
            model_name='event',
            name='event_description',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.DeleteModel(
            name='Date',
        ),
    ]