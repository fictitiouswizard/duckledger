from django.contrib import admin
from bills.models import Bill, Account, Transaction
# Register your models here.


class BillAdmin(admin.ModelAdmin):
    list_display = ["name", "due_date", "amount_due"]


admin.site.register(Bill, BillAdmin)


class AccountAdmin(admin.ModelAdmin):
    list_display = ["name",]


admin.site.register(Account, AccountAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ["transaction_date", "transaction_type", "memo", "amount", "running_balance"]


admin.site.register(Transaction, TransactionAdmin)