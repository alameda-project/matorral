# Generated by Django 2.2.1 on 2019-06-30 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprints', '0005_auto_20190627_2244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sprint',
            options={'get_latest_by': 'created_at', 'ordering': ['updated_at', 'starts_at'], 'verbose_name': 'sprint', 'verbose_name_plural': 'sprints'},
        ),
    ]
