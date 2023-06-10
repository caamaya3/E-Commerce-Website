from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    print("Request!")
    product_objects = Products.objects.all()

    item_name = request.GET.get('item_name')

    if (item_name != '' and item_name is not None):
        product_objects = product_objects.filter(title__icontains=item_name)
    paginator = Paginator(product_objects, 4)
    print(request.GET)
    page = request.GET.get('page')
    print("paginator")
    print(page)
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects': product_objects})
