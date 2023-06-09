# Generated by Django 4.1 on 2023-05-09 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="brand",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to="products.brand",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="products",
            name="name",
            field=models.CharField(max_length=80, verbose_name="Name"),
        ),
    ]
