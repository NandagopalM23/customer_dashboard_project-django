from django.urls import path
from . import views
urlpatterns = [
    path('customer', views.Customer_entry,name='customer'),
]