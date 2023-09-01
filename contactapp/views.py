from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.
def homePage(request):
    return render(request, 'app/home.html')

def loginPage(request):
    if request.method == 'POST':
        userdetails = UserLogin.objects.get(username=request.POST['username'], password=request.POST['password'])
        request.session['firstname'] = userdetails.firstname
        request.session['lastname'] = userdetails.lastname
        request.session['id'] = userdetails.id
        return redirect('home')
    return render(request, 'app/login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        savedata = UserLogin(username=username, password=password, firstname=firstname, lastname=lastname)
        savedata.save()
        messages.success(request, "User registered")
        return redirect('login')
    return render(request, 'app/register.html')


def addnewPage(request):
    if request.method == 'POST':
        myid = request.session['id']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        relationship = request.POST['relationship']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        savedata = Contact(userid=myid, firstname=firstname, lastname=lastname, relationship=relationship, email=email, address=address, phone=phone)
        savedata.save()
    return render(request, 'app/addnew.html')

def viewList(request):
    sid = request.session['id']
    contactlist = Contact.objects.filter(userid=sid)
    context = {'contactlist': contactlist}
    return render(request, 'app/view_list.html', context)

def search(request):
    fn = request.GET.get('firstname')
    contactlist = Contact.objects.filter(firstname__icontains=fn)
    context = {'contactlist': contactlist}
    return render(request, 'app/view_list.html', context)
