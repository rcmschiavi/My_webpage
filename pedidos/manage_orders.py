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

def add_item_order(item_id, order_id, amount):
    """ Função que servirá para adicionar itens 
        pelo usuário na interface
        Aqui é verificado se a quantidade do item é multiplo do que foi estipulado
    """
    product = Product.objects.get(id=item_id)
    multiplier = product.multiplier
    if(amount%multiplier==0):
        order = Order.objects.get(id=order_id)
        OrderDetails.objects.create(order = order, product=product, amount = amount)
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
    # Criar depois de implementar testes

def create_order(client_id):
    order = Order(client_id=client_id)
    order.save()
    return order.id

def list_orders_clients(client_id):
    order = Order.objects.filter(ID=client_id)
