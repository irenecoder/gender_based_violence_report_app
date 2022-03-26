from django import forms

from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['report_title','crime_location','type_of_crime','crime_description','crime_date','phone_no']
        # labels = {'text':''}