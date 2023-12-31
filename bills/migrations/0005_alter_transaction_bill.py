# Generated by Django 5.0 on 2023-12-22 22:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bills", "0004_alter_transaction_transaction_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="bill",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="payments",
                to="bills.bill",
            ),
        ),
    ]
