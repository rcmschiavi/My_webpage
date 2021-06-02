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
    orders = manage_orders.list_orders()
    manage_orders.get_order(orders[1]['id'])
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
    print(request.body)
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
