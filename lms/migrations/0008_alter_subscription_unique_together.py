# Generated by Django 5.1 on 2024-08-20 17:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0007_subscription"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="subscription",
            unique_together={("user", "course")},
        ),
    ]