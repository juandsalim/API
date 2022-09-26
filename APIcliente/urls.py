from django.urls import path
from .views import clienteListView

urlpatterns = [
    path('cliente/',clienteListView.as_view(), name='cliente_list'),
]

