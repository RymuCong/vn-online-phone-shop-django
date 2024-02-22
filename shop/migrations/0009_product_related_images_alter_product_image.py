# Generated by Django 4.2.3 on 2023-10-19 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0008_product_quantity_alter_product_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="related_images",
            field=models.CharField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, upload_to="products"),
        ),
    ]