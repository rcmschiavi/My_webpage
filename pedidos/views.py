from django.shortcuts import render
from pedidos import manage_orders
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
import json

# Decorator que garante o envio do cookie csrf
@ensure_csrf_cookie
def application_page(request):
    clients = manage_orders.list_clients()
    products = manage_orders.list_products()
    orders = manage_orders.list_detailed_order_formated()

    #for order in orders:
        
    
    context = {
        'clientsList': clients,
        'products': products,
        'orders': orders
    }

    return render(request, 'pedidos/index.html', context)

@csrf_protect
def post_order(request):
    data = json.loads(request.body)
    order_id = manage_orders.create_order(data['client_id'])
    for item in data['order_list']:
        manage_orders.add_item_order(item['id'], order_id, int(item['amount']), float(item['price']))
    response = HttpResponse()
    response.status_code = 200
    if False:
        #Criar condição de erro
        pens = []
        response = HttpResponse(json.dumps({'pens': pens, 'err': 'some custom error message'}), 
        content_type='application/json')
        response.status_code = 400
    return response


def add_item_order(request):
    data = json.loads(request.body)
    print(data)
    manage_orders.add_item_order(int(data['item_id']), int(data['order_id']), int(data['amount']), float(data['price']))
    response = HttpResponse()
    response.status_code = 200
    return response

def remove_item_order(request):
    data = json.loads(request.body)
    print("aaalla")
    print(data)
    manage_orders.remove_item_order_by_id(data['item_order_id'])
    response = HttpResponse()
    response.status_code = 200
    return response