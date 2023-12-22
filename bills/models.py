from django.db import models

# Create your models here
TransactionTypes = {
    "ACH": "ACH",
    "DC": "Debit Card",
    "CHK": "Check",
    "CC": "Credit Card",
    "DPST": "Deposit",
}


class Account(models.Model):
    name = models.CharField(max_length=200)
    is_cc = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Bill(models.Model):
    name = models.CharField(max_length=200)
    due_date = models.IntegerField(null=True)
    description = models.TextField(blank=True)
    amount_due = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)
    account = models.ForeignKey("Account", on_delete=models.PROTECT, related_name="bills", null=True)

    def __str__(self):
        return f"{self.name} ({self.amount_due})"


class Transaction(models.Model):
    transaction_date = models.DateField()
    transaction_type = models.CharField(max_length=4, choices=TransactionTypes)
    check_number = models.PositiveIntegerField(null=True, blank=True)
    memo = models.CharField(max_length=199)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    running_balance = models.DecimalField(decimal_places=2, max_digits=10)
    ordinal_number = models.PositiveIntegerField()
    account = models.ForeignKey("Account", on_delete=models.PROTECT, related_name="transactions")
    bill = models.ForeignKey("Bill", on_delete=models.PROTECT, related_name="payments", null=True, blank=True)


