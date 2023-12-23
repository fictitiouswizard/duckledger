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

