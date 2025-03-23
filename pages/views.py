from django.shortcuts import render,redirect
from .models import Login , Film
import time
# Create your views here.


def loginform(request):
    if request.method == 'POST': # check the type of request method
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email') # get the user_email value from the key that i have made it in login page form
        user_password = request.POST.get('user_password') # get the user_password value from the key that i have made it in login page form
        user_data = Login(name = user_name,email = user_email,password = user_password)
        user_data.save()
        time.sleep(2)
        return redirect('options') # this function will direct the user to (movies page)         
    return render(request,'pages/loginForm.html')


def movies(request):
    return render(request , 'pages/movies.html',{'movie':Film.objects.all()})

def signup(request):
    errors = {} # dictionary to get the errors if exist while user filling the form in sign-up page
    if request.method == 'POST': # check the type of request method
        user_name = request.POST.get('user_name') # get the user_name value from the key that i have made it in login page
        user_email = request.POST.get('user_email')# get the user_email value from the key that i have made it in login page
        user_password = request.POST.get('user_password')# get the user_password value from the key that i have made it in login page
        if not user_name or user_name.isdigit() or len(user_name) < 3 or len(user_name) > 20: # check the name field in form
            # create a key in errors and give it a value to use this value in sign-up page
            errors['user_name'] = 'sorry,your name must be characters , not numbers and (bigger than or equal 3 and smaller than or equal 20)'
        if not user_email or '@' not in user_email and '-' in user_email:  # check the email field in form
             # create a key in errors and give it a value to use this value in sign-up page
            errors['user_email'] = 'your email must contain (@) and only symbols(!#$%&*_)'
        if not user_password and len(user_password) < 8 or len(user_password) > 20: # check the password field in form
            # create a key in errors and give it a value to use this value in sign-up page
            errors['user_password'] = 'your password length must be at least 8 and maximum 20'
            # create a key in errors and give it a value to use this value in sign-up page
        if not errors:
            data = Login.objects # get objects from table Login
            # check that user_name,user_email are exist in database (Login table)
            if data.filter(name__exact = user_name , email__exact = user_email).exists():
                # create a key in errors and give it a value to use this value in sign-up page
                errors['user_already_exists'] = f"sorry, your name {user_name} and email {user_email} are already exists.You Can Create New (Name and Email)"
            else:
                user_data = Login(name = user_name , email = user_email , password = user_password)
                user_data.save() # save user data in database
                time.sleep(2)
                return redirect('movies')
    return render(request,'pages/signup.html',{'errors':errors})

def series(request):
    return render(request,'pages/home.html')

def anime(request):
    return render(request,'pages/anime.html')


def options(request):
    return render(request,'pages/options.html')

def landing(request):
    return render(request,'pages/landing.html')

