from django.shortcuts import render, get_object_or_404, redirect
from .models import Cake
from .forms import CakeForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail.message import EmailMessage
from django.core import mail
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from  .forms import signupform,loginform
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout






def create_cake(request):
    if request.method == 'POST':
        form = CakeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_cakes')
    else:
        form = CakeForm()
    return render(request, 'create_cake.html', {'form': form})

def home_cakes(request):
    cakes = Cake.objects.all()
    return render(request, 'homes.html', {'cakes': cakes})

def view_cake(request, pk):
    cake = get_object_or_404(Cake, pk=pk)
    return render(request, 'view_cake.html', {'cake': cake})

def update_cake(request, pk):
    cake = get_object_or_404(Cake, pk=pk)
    if request.method == 'POST':
        form = CakeForm(request.POST, request.FILES, instance=cake)
        if form.is_valid():
            form.save()
            return redirect('view_cake', pk=cake.pk)
    else:
        form = CakeForm(instance=cake)
    return render(request, 'update_cake.html', {'form': form})

def delete_cake(request, pk):
    cake = get_object_or_404(Cake, pk=pk)
    if request.method == 'POST':
        cake.delete()
        return redirect('list_cakes')
    return render(request, 'delete_cake.html', {'cake': cake})

def About(request):
    return render(request, 'about.html')



def all_cakes(request):
    cakes = Cake.objects.all()
    return render(request, 'allcakes.html', {'cakes': cakes})



def send_gmail(request):
     if request.method == 'POST':
         name = request.POST.get('name')
         email = request.POST.get('email')
         phone = request.POST.get('phone')
         message = request.POST.get('message')
         print(name,email,phone,message)

         '''subject = ('name of the person :',name + 'Email of the person: ',email +'contact number of the person:', phone )'''

         subject = 'Contact form'

         message = f'name of the person: {name}, \n  Email of the person: {email}, \n contact number of the person: {phone}, \n message from the person: {message} ' 

         

         send_mail(
             subject,
            
             
             message,
             'kunzoro34@gmail.com',
             ['popsonemmanuel99@gmail.com'],
             fail_silently=False,
             
         )
          
         return HttpResponseRedirect(reverse('list_cakes'))
         
     else:
         
          
         return render(request,'contact.html')



#logout
def user_logout(request):
    logout(request)
    return redirect('list_cakes')

#signup
def user_signup(request):
 if request.method == "POST":
    form = signupform(request.POST)
    if form.is_valid():
        messages.success(request, "Congratulations!! Welcome to Cake Box. ")
        user= form.save()
        
 else:
  form = signupform()
 return render(request, 'signup.html', {'form':form})

#login
def user_login(request):
 if not request.user.is_authenticated:
      if request.method == "POST":
            form = loginform( data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'logged in successfully !!')
                    #return HttpResponseRedirect('/list_cakes/')
                    return redirect('list_cakes')
      else:
            form = loginform()
      return render(request, 'login.html', {'form': form})
 else:
    return HttpResponseRedirect('')