# Generated by Django 4.1.5 on 2023-02-02 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="date_published",
            field=models.DateField(null=True, verbose_name="Date Published"),
        ),
        migrations.AddField(
            model_name="book",
            name="image",
            field=models.ImageField(null=True, upload_to="", verbose_name="Image"),
        ),
        migrations.AlterField(
            model_name="book",
            name="description",
            field=models.TextField(
                max_length=1000, null=True, verbose_name="Description"
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(max_length=200, null=True, verbose_name="Title"),
        ),
    ]
