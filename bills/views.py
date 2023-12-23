from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from bills.models import Bill, Transaction


def list_bills(request):
   bills = Bill.objects.all()
   transactions = Transaction.objects.all()
   return render(
      request,
      "bills/bill_list.html",
      {
         "bills": bills,
         "transactions": transactions
      }
   )


def create_transaction(request):
   # print(request.POST["transaction_date"])
   transaction = Transaction(**request.POST)
   transactions = Transaction.objects.all()
   return render(
      request,
      'bills/partials/transaction_list.html',
      {
         "transactions": transactions
      }
   )

