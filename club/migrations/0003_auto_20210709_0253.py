# Generated by Django 3.1.4 on 2021-07-08 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cultboard', '0002_auto_20210707_2258'),
        ('club', '0002_auto_20210709_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='welcomenote',
            name='club',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cultboard.club'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='status',
            field=models.IntegerField(choices=[(1, 'Publish'), (0, 'Draft')], default=0),
        ),
    ]