from django.conf.urls import url
from pedidos import views as pedidos_views

urlpatterns = [
    url('pedidos', pedidos_views.application_page, name='Pedidao'),
    url('save_order', pedidos_views.post_order, name='post_order'),
    url('add_item', pedidos_views.add_item_order, name='add_item'),
    url('remove_item', pedidos_views.remove_item_order, name='remove_item')
]
