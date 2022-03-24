from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Report


def index(request):
    return render(request, 'index.html')

# @login_required(login_url='useraccounts:login')
def post_report(request):
    if request.method == 'POST':
        type_of_crime = request.POST.get('type_of_crime')
        crime_description = request.POST.get('crime_description')
        crime_location = request.POST.get('crime_location')
        crime_date = request.POST.get('crime_date')

        messages.info(request, 'Once the crime has been submitted, you cannot edit or delete it.')
        # return redirect('confirm')
        
        report_crime_save = Report.objects.create(type_of_crime=type_of_crime, crime_description=crime_description, crime_location=crime_location, date_of_crime=crime_date)
        report_crime_save.save()
        messages.success(request, 'Crime {} has been submitted successfully.'.format(type_of_crime))
        return redirect('reports')

    return render(request, 'post.html')

# @login_required(login_url='useraccounts:login')
def reports(request):

    #show all topics
    reports = Report.objects.order_by('crime_date')
    context={'reports': reports}
    return render(request,'reports.html',context)
@login_required(login_url='useraccounts:login')
def report(request,report_id):
    #show a single topic and all its entries
    report = Report.objects.get(id=report_id)
    context = {'report':report}
    return render(request,'report.html',context)

# def confirm_submission(request):
#     report_gbv_crime(request)
    
#     return render(request, 'confirm_submission.html')

# def crime_history(request):
#     crimes = Report.objects.all()
#     context = {'crimes_reported': crimes}
    
#     return render(request, 'user_crime-rep-hist.html', context)
