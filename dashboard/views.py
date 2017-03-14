from django.shortcuts import render
from django.http import HttpResponse
from .scripts import basic_info

def index(request):
    system_data = [
        basic_info.get_processor(),
        basic_info.get_platform(),
        basic_info.get_physical_memory(),
    ]

    context = {'system_data': system_data}
    return render(request, 'dashboard/index.html', context)