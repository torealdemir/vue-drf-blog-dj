# Generated by Django 5.0 on 2024-02-14 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_note_alter_blog_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Note',
        ),
    ]