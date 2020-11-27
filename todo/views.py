from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth import authenticate, login
from accounts.forms import FormLogin
from .models import competitor
from .models import competition

# Create your views here.

def index(request):
	return render(request, "index.html")

def RegisterPage(request):
	return render(request, "competitorRegister.html")

def AccountLogin(request):
	return render(request, "accounts/form.html")

def CompetitionPage(request):
	competitions = competition.objects.all 
	return render(request, "competitionPage.html",{"competitions":competitions})

def MemberPage(request):
	Members = competitor.objects.all
	return render(request, "memPage.html",{"Members":Members})

def registerSend(request):
	if request.method == "GET":
		return redirect("/")


	else:
		_tc = request.POST.get("RegisterTcNo")
		_name = request.POST.get("RegisterName")
		_surname = request.POST.get("RegisterSurname")
		_school = request.POST.get("RegisterSchool")
		_faculty = request.POST.get("RegisterFaculty")

		newcompetitor = competitor(tcNumber = _tc, name = _name, surname = _surname, school = _school, faculty = _faculty, compeleted = False)

		newcompetitor.save()
		return redirect("/")

def competitionSend(request):
	if request.method == "GET":
		return redirect("/")

	else:
		_competitionName = request.POST.get("RcompetitionName")
		_competitionComment = request.POST.get("RcompetitionComment")


		newcompetition = competition(competitionName = _competitionName, competitionComment = _competitionComment)

		newcompetition.save()
		return redirect("/")

def LoginwithAccount(request):
	form = FormLogin(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('LUsername')
		password = form.cleaned_data.get('LPassword')

		user = authenticate(username = username, password = password)

		login(request, user)
		return redirect("/")
	return render(request, "accounts/form.html",{'form':form})