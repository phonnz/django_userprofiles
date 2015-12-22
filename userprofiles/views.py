from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView


from .models import User

def home(request):
    return HttpResponse('Vista')

class AllUsersView(ListView):
    model = User
    template_name = 'users.html'
