from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from braces.views import LoginRequiredMixin


from .models import User

def home(request):
    return render(request, 'home.html', {})

## Login required with class based views
class AllUsersView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user_list.html'
    login_url = '/'

    # def get_context_data(self, **kwargs):
    #     # context = {}
    #     # context = general_context(AllUsersView, 'AllUsersView', self, **kwargs)
    #     context['msg'] = 'This is a request context'
    #     return context

    # def get(self, request, *args, **kwargs):
    #     print 'This is a get request'
    #     return HttpResponse('GET')

    def post(self, request, *args, **kwargs):
        print 'This is a  post request'
        return HttpResponse('POST')

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user_detail.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        users = [username for username in User.objects.all()]
        return context

## Login required with function based views
@login_required(login_url = '/')
def signout(request):
    logout(request)
    return HttpResponseRedirect('/')
