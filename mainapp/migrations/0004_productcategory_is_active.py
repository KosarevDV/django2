# Generated by Django 3.2.11 on 2022-02-09 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_alter_product_color"),
    ]

    operations = [
        migrations.AddField(
            model_name="productcategory",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="активна"),
        ),
    ]
