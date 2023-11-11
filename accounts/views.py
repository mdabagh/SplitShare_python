from django.shortcuts import render
from django.contrib.auth.views import LoginView

def login(request):
    return render(request, 'accounts/login.html', {'form': LoginForm()})

class LoginForm(LoginView):
    template_name = 'accounts/login.html'