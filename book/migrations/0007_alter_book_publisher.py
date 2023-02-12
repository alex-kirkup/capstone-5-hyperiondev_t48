# Generated by Django 4.1.5 on 2023-02-08 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("publisher", "0001_initial"),
        ("book", "0006_rename_author_book_authors"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="publisher",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Books",
                to="publisher.publisher",
                verbose_name="Publisher",
            ),
        ),
    ]