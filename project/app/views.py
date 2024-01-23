from django.shortcuts import render, redirect

from .forms import AddProduct
from .models import Product

def create_view(request):
    if request.method == 'POST':
        form = AddProduct(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            create = Product.objects.create(name=name, description=description, price=price)
            create.save()
            return redirect('items')
    form = AddProduct()
    return render(request, 'shop/create_product.html', context={'form': form})
def product_view(request, id):
    product = Product.objects.get(pk=id)

    return render(request, 'shop/product.html', context={'product': product})
def shop_base_view(request):
    products = Product.objects.all()
    return render(request, 'shop/shop.html', context={'products':products})
