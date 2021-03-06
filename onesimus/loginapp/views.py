from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required



    # Redirect to a success page.

# Create your views here.
@login_required
def employeeform(request):
	return render(request, 'loginapp/employee_masterlist.html')



def logoutuser(request):
    logout(request)  
