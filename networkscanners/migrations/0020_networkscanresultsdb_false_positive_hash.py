# Generated by Django 3.1.8 on 2021-05-31 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("networkscanners", "0019_auto_20210531_2000"),
    ]

    operations = [
        migrations.AddField(
            model_name="networkscanresultsdb",
            name="false_positive_hash",
            field=models.TextField(blank=True, null=True),
        ),
    ]
