from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse

from products.models import Product
from .models import Basket

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
@login_required
def basket_add(request, product_id):
    products = Product.objects.all()
    if is_ajax(request=request):
        product = Product.objects.get(id=product_id)
        baskets = Basket.objects.filter(user=request.user, product=product_id)

        if not baskets:
            Basket.objects.create(user=request.user, product=product, quantity=1)
        else:
            basket = baskets.first()
            basket.quantity += 1
            if basket.quantity <= product.quantity:
                basket.save()
        context = {
            'baskets': baskets,
            'products': products
        }
        result = render_to_string('products/product_list.html', context)
        return JsonResponse({'result': result})

@login_required
def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



@login_required
def basket_edit(request, id, quantity):
    if is_ajax(request=request):
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Basket.objects.filter(user=request.user)
        context = {
            'baskets': baskets
        }
        result = render_to_string('basket/basket.html', context)
        return JsonResponse({'result': result})