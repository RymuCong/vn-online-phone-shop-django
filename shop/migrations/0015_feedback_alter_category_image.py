# Generated by Django 4.2.3 on 2023-10-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0014_alter_category_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("customer_name", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("comment", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(upload_to="category/"),
        ),
    ]
