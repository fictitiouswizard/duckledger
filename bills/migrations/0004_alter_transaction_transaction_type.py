# Generated by Django 5.0 on 2023-12-22 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bills", "0003_transaction"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="transaction_type",
            field=models.CharField(
                choices=[
                    ("ACH", "ACH"),
                    ("DC", "Debit Card"),
                    ("CHK", "Check"),
                    ("CC", "Credit Card"),
                    ("DPST", "Deposit"),
                ],
                max_length=4,
            ),
        ),
    ]