
from django.urls import path
from useraccounts.views import *
# from gbvcrimereportapp.views import *
app_name='useraccounts'
urlpatterns = [
    path('login/', loginPage, name='login'),
    path('register/',registerPage, name='register'),
    path('logout/', logout, name='logout'),
    
]