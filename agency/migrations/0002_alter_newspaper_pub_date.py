# Generated by Django 5.0.4 on 2024-04-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("agency", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newspaper",
            name="pub_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
