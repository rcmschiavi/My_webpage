from pedidos.models import Client, Product, Order, OrderDetails


def get_order(order_id):
    order = Order.objects.get(ID=order_id)
    products = order.orderdetails_set.all().values()
    return products

def add_item_order(item_id, order_id, amount):
    product = Product.objects.get(ID=item_id)
    order = Order.objects.get(ID=order_id)
    OrderDetails.objects.create(ORDER = order, PRODUCT=product, QUANTITY = amount)

def remove_item_order(item_id, order_id):
    product = Product.objects.get(ID=item_id)
    order = Order.objects.get(ID=order_id)
    order.PRODUCTS.remove(product)

def edit_item_amount(item_id, order_id):
    product = Product.objects.get(ID=item_id)
    order = Order.objects.get(ID=order_id)
    # Criar depois de implementar testes

def create_order(client_id):
    order = Order(CLIENT_id=client_id)
    order.save()

def list_orders_clients(client_id):
    order = Order.objects.filter(ID=client_id)
