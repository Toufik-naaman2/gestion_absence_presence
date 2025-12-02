from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'

# @login_required
def loginPage(request):
    return render(request, 'auth/login.html')

# test
def home(request):
    return HttpResponse("hello world")
