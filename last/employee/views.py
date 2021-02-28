from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from employee.models import *
from .forms import UserLogin,UserAddForm



def login_view(request):
	login_user = request.user
	if request.method == 'POST':
		form = UserLogin(data = request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username = username, password = password)
			if user and user.is_active:
				login(request,user)
				if login_user.is_authenticated:
					return redirect('dashboard:dashboard')
			else:
			    messages.error(request,'Account is invalid',extra_tags = 'alert alert-error alert-dismissible show' )
			    return redirect('employee:login')

		else:
			return HttpResponse('data not valid')

	dataset=dict()
	form = UserLogin()

	dataset['form'] = form
	return render(request,'employee/login.html',dataset)




def logout_view(request):
	logout(request)
	return redirect('employee:login')



def users_list(request):
	employees = Employee.objects.all()
	return render(request,'employee/users_table.html',{'employees':employees,'title':'Users List'})



