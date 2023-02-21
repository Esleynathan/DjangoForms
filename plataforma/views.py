from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from forms import Cliente

@login_required(login_url= '/auth/login')
def home(request):
        form = Cliente.form
        return render(request, 'home.html', {'form': form})
