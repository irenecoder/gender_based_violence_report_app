from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import auth
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
import sys


sys.setrecursionlimit(1500)
def register(request):
    if request.user.is_authenticated:
        return redirect('gbvcrimereportapp:index')
    else:
        form = CreateUserForm()

        if request.method=='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'account was created for '+user)
                return redirect('login')

        context={'form':form}
        return render(request,'register.html',context)
def login(request):
    if request.user.is_authenticated:
        return redirect('gbvcrimereportapp:index')
    else:

        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request,'username or password is incorrect')
                context={}
                return render(request,'login.html',context)
        context={}
        return render(request,'login.html',context)
def logout(request):
    auth.logout(request)
    # messages.info(request)
    return redirect('gbvcrimereportapp:index')
# def logout(request):
#     logout(request)
#     return redirect('gbvcrimereportapp:index')

# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.models import auth,User

# from useraccounts.models import Users


# def register(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         user_mobile_no = request.POST['phone']
#         email_addr = request.POST['email']
#         gender = request.POST['gender']
#         password1 = request.POST['password']
#         confirm_password = request.POST['c_password']

#         if len(password1) < 8:
#             if len(confirm_password) < 8:
#                 messages.warning(request, 'Password too short.')
#                 return redirect('register')

#         elif password1 != confirm_password:
#             messages.warning(request, 'Passwords not matching.')
#             return redirect('register')
#         elif User.objects.filter(username=name).exists():
#             messages.error(request, 'Username already taken.')
        
#             if User.objects.filter(email=email_addr).exists():
#                 messages.error(request, 'Email Address already taken.')
#                 return redirect('register')
        
#         else:
#             user_acc_reg = Users.objects.create(name=name, gender=gender, email_address=email_addr, phone_no=user_mobile_no)
#             user_acc_reg.save()     # save user details in Users table in database.

#             auth_user_acc_registration = User.objects.create_user(username=name, email=email_addr, password=password1)
#             auth_user_acc_registration.save()   # save user details in django's auth_users table.

#             messages.success(request, 'User {} registered successfully!'.format(name))
#             return redirect('login')

#     return render(request, 'register.html')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['name']
#         password1 = request.POST['password']

#         login = auth.authenticate(name=username, password=password1)

#         if login is not None:
#             auth.login(request,login)
#             messages.info(request, 'Welcome back!')
#             return redirect('index')
        
#         else:
#             # Check if the user has an accoi=unt but has entered an incorrect password.
#             if password1 != auth.authenticate(password=password1) and User.objects.filter(username=username).exists():
#                 messages.error(request, 'Incorrect Password! Please try again.')
#                 return redirect('login')
#             else:   # if the user is not registered, display this message.
#                 messages.error(request, 'Invalid Credentials! Create an account to access our website.')
#                 return redirect('login')

#     return render(request, 'login.html')


# def logout(request):
#     auth.logout(request)
#     messages.info(request)