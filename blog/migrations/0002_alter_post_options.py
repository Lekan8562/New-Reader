# Generated by Django 4.1.7 on 2024-01-08 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-publish', '-updated']},
        ),
    ]