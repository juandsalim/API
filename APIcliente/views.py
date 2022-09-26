from django.shortcuts import render
from django.views import View
from .models import cliente
from django.http import JsonResponse

class clienteListView(View):
    def get (self, request):
        clist = cliente.objects.all()
        return JsonResponse(list(clist.values()), safe=False)

