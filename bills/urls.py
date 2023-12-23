from django.urls import path

from . import views

urlpatterns = [
    path("bills/", views.list_bills, name="bills.list"),
    path("transaction/create", views.create_transaction, name="transaction.create")
]