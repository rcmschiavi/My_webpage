from django.test import TestCase
from pedidos.models import Client, Product, Order, OrderDetails
from pedidos import manage_orders


class OrderTestCase(TestCase):

    def setUp(self):
        # Adiciona clientes ao banco de dados de teste
        Client.objects.create(name="Darth Vader")
        Client.objects.create(name="Obi-Wan Kenobi")
        # Adiciona produtos ao banco de dados de teste
        Product.objects.create(name="Millenium Falcon", sugested_price=550000.00, multiplier=1)
        Product.objects.create(name="X-Wing", sugested_price=60000.00, multiplier=2) 
        # Cria o primeiro pedido fictício
        self.order_one_id = manage_orders.create_order(2)
        # Adiciona itens com quantidade correta ao primeiro pedido
        manage_orders.add_item_order(item_id=2, order_id=self.order_one_id, amount=4)
        manage_orders.add_item_order(item_id=1, order_id=self.order_one_id, amount=5)

        self.order_two_id = manage_orders.create_order(1)
        # Adiciona um item com quantidade incorreta e outro com a correta
        manage_orders.add_item_order(item_id=2, order_id=self.order_two_id, amount=9)
        manage_orders.add_item_order(item_id=1, order_id=self.order_two_id, amount=7)

    def test_case(self):
        # Teste e condições do primeiro pedido
        products_order_one = manage_orders.get_order(self.order_one_id)
        expected_order_one_return = [{'item': 'X-Wing', 'amount': 4}, 
        {'item': 'Millenium Falcon', 'amount': 5}]
        self.assertEqual(products_order_one, expected_order_one_return)
        # Teste e condições do segundo pedido
        products_order_two = manage_orders.get_order(self.order_two_id)
        expected_order_two_return = [{'item': 'Millenium Falcon', 'amount': 7}]
        self.assertEqual(products_order_two, expected_order_two_return)

        # Teste e condições do primeiro pedido após remoção de 1 item
        manage_orders.remove_item_order(item_id=2, order_id=1)
        products_order_one = manage_orders.get_order(1)
        expected_order_one_return = [{'item': 'Millenium Falcon', 'amount': 5}]
        self.assertEqual(products_order_one, expected_order_one_return)
        
