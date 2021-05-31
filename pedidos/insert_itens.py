from pedidos.models import Client, Product, Order, OrderDetails

def insert_clients():
    clients = ["Darth Vader", "Obi-Wan Kenobi", "Luke​ ​Skywalker", "Imperador​ ​Palpatine", "Han Solo"]
    for client in clients:
        client_row = Client(name = client)
        client_row.save()

def insert_products():
    products = [["Millenium​ ​Falcon", 550000.00, 1],["X-Wing",60000.00, 2],
    ["Super Star Destroyer", 4570000.00, 1],["TIE Fighter", 75000.00, 2],
    ["Lightsaber", 6000.00, 5],["DLT-19 Heavy Blaster Rifle", 5800.00, 1],
    ["DL-44 Heavy Blaster Pistol", 1500.00, 10]]
    for product in products:
        product_row = Product(name=product[0], sugested_price=product[1], multiplier=product[2])
        product_row.save()