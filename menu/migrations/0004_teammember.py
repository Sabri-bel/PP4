# Generated by Django 4.2.19 on 2025-02-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_feedback_options_alter_post_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('bio', models.TextField()),
            ],
        ),
    ]
