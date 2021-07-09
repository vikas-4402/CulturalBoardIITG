# Generated by Django 3.1.4 on 2021-07-06 20:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cultboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WelcomeNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='media/images')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cultboard.club')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=100)),
                ('content', models.TextField()),
                ('expired_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cultboard.club')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(1, 'Publish'), (0, 'Draft')], default=0)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cultboard.club')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Achieve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=200)),
                ('image', models.ImageField(default='default.jpg', upload_to='media/achieve')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cultboard.club')),
            ],
        ),
    ]
