# Generated by Django 4.1.1 on 2022-09-12 01:05

from django.db import migrations, models
import reviews.models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.PositiveIntegerField(
                validators=[reviews.models.Review.validate_rating]
            ),
        ),
    ]
