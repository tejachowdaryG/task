from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect 

from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group
# Create your views here.
from account.forms import *

from .models import *

from .decorators import unathentictaed_uder, allowed_users, admin_only



def registerPage(request):	
	form = CreateUserForm()
	if request.method=="POST":
		form=CreateUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='Team_leader')
			user.groups.add(group)

		return HttpResponseRedirect('/login')
	return render(request,'accounts/signup.html',{'form':form})

def loginPage(request):
	if request.method =="POST":
		username =request.POST.get('username')
		password=request.POST.get('password')

		user = authenticate(request, username=username,password=password)

		if user is not None:
			login(request, username)
			return redirect('/home')

		else:
			messages.info(request,'username or pasword is requried')


	context ={}
	return render(request,'registration/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def home(request):
	TL=Team_task.objects.all()
	TM=Team_model.objects.all()

	total_TeamMembers= TM.count()
	assinged =TL.filter(status='assigned').count()
	pending = TL.filter(status='pending').count()
	return render(request,'accounts/dashboard.html')


@login_required(login_url='login')
@admin_only
def userpage(request):
	team_task= request.user.Team_task.drder_set.all()
	print('Team_tasK:',team_task)

def Team_taskView(request):
	TL=Team_task.objects.all()
	return render(request,'accounts/task.html',{'TL':TL})



def  Team_modelView(request):
	 TM=Team_model.objects.all()
	 return render(request,'accounts/model.html',{'TM':TM})

@login_required(login_url='login')
@admin_only
def Team_taskFormView(request):
	Task_form=Team_taskForm()
	if request.method=="POST":
		Task_form=Team_taskForm(request.POST)
		if Task_form.is_valid():
			Task_form.save()
	return render(request,'accounts/Taskform.html',{'f':Task_form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['team_leader'])
def Team_modelFormView(request):
	model_form=Team_modelForm()
	if request.method=="POST":
		model_form=Team_modelForm(request.POST)
		if model_form.is_valid():
			model_form.save()
			return redirect('TL')
	return render(request,'accounts/modelForm.html',{'m':model_form})


@login_required(login_url='login')
@allowed_users(allowed_roles=['team_leader'])
def Team_taskUpdateView(request,id):
	TL=Team_task.objects.get(id=id)
	if request.method=="POST":
		TL=Team_taskForm(request.POST,instance=TL)
		if TL.is_valid():
			TL.save()
			return redirect('/TL')
	return render(request,'accounts/taskupdateform.html',{'L':TL})

@login_required(login_url='login')
@allowed_users(allowed_roles=['team_leader'])
def Team_modelUpdateView(request,id):
	TM=Team_model.objects.get(id=id)
	if request.method=="POST":
		TM=Team_modelForm(request.POST,instance=TM)

		if TM.is_valid():
			TM.save()
			return redirect('/TM')
	return render(request,'accounts/modelupdateform.html',{'M':TM}) 

@login_required
@allowed_users(allowed_roles=['team_leader'])
def Team_taskDelete(request,id):
	emp=Team_task.objects.get(id=id)
	emp.delete()
	return redirect('/TL')
@login_required(login_url='login')
@allowed_users(allowed_roles=['team_leader'])
def Team_modelDelete(request,id):
	emp=Team_model.objects.get(id=id)
	emp.delete()
	return redirect('/TM')