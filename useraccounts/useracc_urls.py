
from django.urls import path
from useraccounts.views import *
# from gbvcrimereportapp.views import *
app_name='useraccounts'
urlpatterns = [
    path('login/', login, name='login'),
    path('register/',register, name='register'),
    path('logout/', logout, name='logout'),
    
]