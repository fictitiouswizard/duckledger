from django.urls import path

from . import views

urlpatterns = [
    path("bills/", views.list_bills, name="bills.list")
]