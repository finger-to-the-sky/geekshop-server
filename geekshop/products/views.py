from django.shortcuts import render
import json

def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)

def products(request):

    with open('/home/zagmak/PycharmProjects/geekshop-server/geekshop/products/fixtures/products.json', 'r',
              encoding='UTF-8') as f:
        data = json.load(f)

    context = {
        'title': 'GeekShop - Продукты',
        'products': []
    }
    for item in data:
        context['products'].append(item['fields'])

    return render(request, 'products/products.html', context)
