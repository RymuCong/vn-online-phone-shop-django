# Generated by Django 4.2.3 on 2023-10-20 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0012_remove_product_related_images"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="image",
            field=models.ImageField(blank=True, upload_to="category"),
        ),
    ]
