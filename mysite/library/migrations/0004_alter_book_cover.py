# Generated by Django 4.1.1 on 2022-09-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0003_book_cover"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="cover",
            field=models.ImageField(
                null=True, upload_to="covers/", verbose_name="Viršelis"
            ),
        ),
    ]
