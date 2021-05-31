from django.conf.urls import url
from pedidos import views as pedidos_views

urlpatterns = [
    url('pedidos', pedidos_views.application_page, name='Pedidão')
]
