# Generated by Django 5.0 on 2023-12-22 22:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bills", "0006_alter_transaction_check_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="bill",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="payments",
                to="bills.bill",
            ),
        ),
    ]