from django.shortcuts import render
from pedidos import manage_orders

# Create your views here.
def application_page(request):
    clients = manage_orders.list_clients()
    products = manage_orders.list_products()
    context = {
        'clientsList': clients,
        'products': products
    }
    print(context)
    return render(request, 'pedidos/index.html', context)