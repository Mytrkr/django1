from django.shortcuts import render, redirect
from .forms import FormLogin
from django.contrib.auth import authenticate, login


def _Login(request):
	form = FormLogin(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('LUsername')
		password = form.cleaned_data.get('LPassword')

		user = authenticate(username = username, password = password)

		login(request, user)
		return redirect("/")
	return render(request, "accounts/form.html",{'form':form})
# Create your views here.
