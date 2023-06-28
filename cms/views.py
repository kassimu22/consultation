from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from .EmailBackEnd import EmailBackEnd
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def homepage(request):
    return render(request, 'cms/home.html')

def showLoginPage(request):
    return render(request, 'cms/login.html')

def dblogin(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Method not Allowed</h2>')
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"),
                                         password=request.POST.get("password"))
        if user != None:
            login(request, user)  # attach user authentication to the session login function
            if user.user_type == "1":
                return HttpResponseRedirect('/admin_dashboard')
                # return HttpResponse("Email :"+request.POST.get('email')+" Password: "+request.POST.get('password'))
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("staff_panel"))
            else:
                return HttpResponseRedirect(reverse("student_panel"))
            # return HttpResponse("Email :"+request.POST.get('email')+" Password: "+request.POST.get('password'))
            # return HttpResponseRedirect('/admin_dashboard')
        else:
            messages.error(request, 'Invalid email or password')
            return HttpResponseRedirect("login")

def getUserDetails(request):
    if request.user != None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse('Please login first')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


