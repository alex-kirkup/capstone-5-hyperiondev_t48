# Generated by Django 4.1.5 on 2023-02-09 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("publisher", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="publisher",
            options={"ordering": ["name"]},
        ),
    ]
