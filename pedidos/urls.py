from django.conf.urls import url
from pedidos import views as pedidos_views

urlpatterns = [
    url('pedidos', pedidos_views.application_page, name='Pedidao'),
    url('save_order', pedidos_views.post_order, name='post_order')
]
