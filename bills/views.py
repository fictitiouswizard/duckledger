from django.shortcuts import render

# Create your views here.

def list_bills(request):
   return render(request, "bills/list_bills.html", {})
