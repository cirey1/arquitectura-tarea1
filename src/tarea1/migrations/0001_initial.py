# Generated by Django 2.1.1 on 2018-09-12 00:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('comment_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('client_ip', models.CharField(max_length=200)),
            ],
        ),
    ]
