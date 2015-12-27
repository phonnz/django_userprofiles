from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from braces.views import LoginRequiredMixin


from .models import User
from .forms import CreateUserForm

def home(request):
    return render(request, 'home.html', {})

## Login required with class based views
class AllUsersView(LoginRequiredMixin, ListView):
    model = User
    ## If we wanna change default object name (object_list) just set context_object_name
    context_object_name = 'users'
    template_name = 'user_list.html'
    login_url = '/'

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
        context['created'] = User.objects.get(pk = context['object'].id).created
        context['users'] = [username for username in User.objects.all()]

        return context

class SlugUserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user_detail.html'
    login_url = '/'
    slug_field = 'username'

    def get_context_data(self, **kwargs):
        context = super(SlugUserDetailView, self).get_context_data(**kwargs)
        context['created'] = User.objects.get(username = context['object'].username).created
        context['users'] = [username for username in User.objects.all()]

        return context

class CreateUserView(CreateView):
    model = User
    template_name = 'register.html'
    ## If you just wanna render form without style and order
    # fields = '__all__'
    ## If you wanna use custom form; You need to create form class in forms.py file
    form_class = CreateUserForm
    success_url = '/users/usuarios/'

    def form_valid(self, form):
        print 'valid'
        return super(CreateUserView, self).form_valid(form)

    def form_invalid(self, form):
        print 'invalid'
        return super(CreateUserView, self).form_invalid(form)


## Login required with function based views
@login_required(login_url = '/')
def signout(request):
    logout(request)
    return HttpResponseRedirect('/')
