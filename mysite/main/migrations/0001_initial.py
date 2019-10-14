# Generated by Django 2.2.6 on 2019-10-14 11:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_title', models.CharField(max_length=100)),
                ('feedback_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Feedback Time')),
                ('feedback_content', models.TextField(help_text='Share Your Ideas Here!')),
                ('feedback_user_id', models.EmailField(max_length=254, verbose_name='Email ID')),
            ],
        ),
    ]
