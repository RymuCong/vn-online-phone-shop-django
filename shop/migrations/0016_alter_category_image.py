# Generated by Django 4.2.5 on 2023-10-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_feedback_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='category'),
        ),
    ]
