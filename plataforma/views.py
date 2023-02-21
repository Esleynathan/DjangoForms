from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import Cliente

@login_required(login_url= '/auth/login')
def home(request):
	form = Cliente()

	input_alterar= ('nome','idade')
	for i in form.fields.keys():
		for i in input_alterar:
			try:
				classe_anterior = form.fields[i].widget.attrs['class']
			except KeyError:
				classe_anterior = ""
				
			form.fields[i].widget.attrs['class'] += classe_anterior + " teste"

	return render(request, 'home.html', {'form': form})
		