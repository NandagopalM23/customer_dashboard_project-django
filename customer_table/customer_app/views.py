# from django.shortcuts import render
# from .models import Customer
# # Create your views here.
# def Customer_entry(request):
#     customer_details=Customer.objects.all()
#     return render(request,'customer_table\customer_app\templates\index.html',{'customer_details':customer_details})


from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Customer_entry(request):
        return HttpResponse("Hello world!")

