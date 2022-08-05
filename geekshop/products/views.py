from django.shortcuts import render
from django.conf import settings
import json
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)

def products(request):
    file_path = settings.BASE_DIR / 'products/fixtures/products.json'

    data = json.load(open(file_path, encoding='UTF-8'))

    context = {
        'title': 'GeekShop - Продукты',
        'products': []
    }
    for item in data:
        context['products'].append(item['fields'])

    return render(request, 'products/products.html', context)
