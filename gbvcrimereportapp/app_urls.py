from django.urls import path

from .views import *

app_name='gbvcrimereportapp'
urlpatterns = [
    path('index/', index, name='index'),
    # path('user_homepage', user_homepage, name='user_homepage'),
    # path('off_homepage', officer_homepage, name='off_homepage'),
    # path('submission', confirm_submission, name='confirm'),
    path('post/', post_report, name='post_report'),
    # path('crime-history', crime_history, name='history'),
    path('reports/',reports,name='reports'),
    # path('report/',report,name='report'), 
    path('report/<int:report_id>/',report,name='report'),
    

]
