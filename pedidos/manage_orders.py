from pedidos.models import Client, Product, Order, OrderDetails


def get_order(order_id):
    """ Função para retornar lista de dicionário contendo itens de pedidos
        Será utilizada para exibir a lista de itens na UI
    """
    order = Order.objects.get(id=order_id)
    products = order.orderdetails_set.all().values().order_by("id")
    details_list = []
    for product in products:
        details = {
            "item": Product.objects.get(id=product["product_id"]).name,
            "amount": product["amount"]
        }
        details_list.append(details)
    return details_list

def add_item_order(item_id, order_id, amount, price):
    """ Função que servirá para adicionar itens 
        pelo usuário na interface
        Aqui é verificado se a quantidade do item é multiplo do que foi estipulado
    """
    product = Product.objects.get(id=item_id)
    multiplier = product.multiplier
    if(amount%multiplier==0):
        order = Order.objects.get(id=order_id)
        OrderDetails.objects.create(order = order, product=product, amount = amount, price = price)
        return True
    else:
        return False

def remove_item_order(item_id, order_id):
    product = Product.objects.get(id=item_id)
    order = Order.objects.get(id=order_id)
    order.products.remove(product)

def edit_item_amount(item_id, order_id):
    product = Product.objects.get(id=item_id)
    order = Order.objects.get(id=order_id)

def create_order(client_id):
    order = Order(client_id=client_id)
    order.save()
    return order.id

def list_orders_clients(client_id):
    order = Order.objects.filter(ID=client_id)

def list_orders():
    orders = list(Order.objects.all().values().order_by("id"))
    print(orders)
    return orders


def list_detailed_orders():
    # TODO gerar lista com detalhes dos pedidos
    return False

def list_clients():
    clients = list(Client.objects.values_list('id','name'))
    details_list = []
    for client in clients:
        details = {
            "id": client[0],
            "name": client[1]
        }
        details_list.append(details)
    return details_list

def get_return_rate_values(suggested_price):
    great = suggested_price + 0.01
    good = round(0.9*suggested_price, 2)
    poor = good-0.01
    return great, good, poor

def list_products():
    products = list(Product.objects.values_list('name', 'sugested_price','multiplier', 'id'))
    details_list = []
    for product in products:
        return_rate = get_return_rate_values(float(product[1]))
        details = {
            "item": product[0],
            "suggested_price": float(product[1]),
            "multiplier": product[2],
            "return_rate": {"great":return_rate[0], "good":return_rate[1], "poor":return_rate[2]},
            "id": product[3]
        }
        details_list.append(details)
    return details_list