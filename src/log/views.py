#log/views.py
from django.shortcuts import render,render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.models import User


def login(request):
	token={}
	token.update(csrf(request))
	return 	render_to_response('login.html',token)


def process_login(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	print(username)
	print(password)
	user=auth.authenticate(username=username,password=password)
	print(user)

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/loggedin')
	else:
		return HttpResponseRedirect('/login_error')

def login_error(request):
	return render_to_response('login_error.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')



# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
#@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")


def loggedin(request):
    return render_to_response('loggedin.html',
                              {'username': request.user})

