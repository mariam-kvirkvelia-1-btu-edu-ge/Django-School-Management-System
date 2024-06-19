# Generated by Django 3.0.8 on 2020-11-24 12:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("staffs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="staff",
            name="mobile_number",
            field=models.CharField(
                blank=True,
                max_length=13,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Entered mobile number isn't in a right format!",
                        regex="^[0-9]{9,15}$",
                    )
                ],
            ),
        ),
    ]
