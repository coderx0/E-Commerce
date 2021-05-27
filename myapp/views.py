from django.shortcuts import render
from store.models import Product
# Create your views here.
def index(request):
    products = Product.objects.all().filter(is_available = True)
    context = {
        'products':products,
    }
    return render(request,'home.html',context)