from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from useraccounts.models import Users

class Report(models.Model):
    # crimeid = models.ForeignKey(Users, on_delete=models.CASCADE)
    report_title = models.CharField(max_length=100)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    # num_reported = models.PositiveIntegerField()
    crime_location = models.CharField(max_length=100)
    type_of_crime = models.CharField(max_length=100)
    crime_description = models.CharField(max_length=100)
    crime_date = models.DateTimeField(default=timezone.now)
    phone_no= models.IntegerField()


    # class Meta:
    #     verbose_name = 'Reported Crimes'
    #     verbose_name_plural = verbose_name

    def __str__(self):
        return 'Crime {} was reported on {}'.format(self.type_of_crime, self.crime_date.strftime('%a %dth-%m-%Y %H:%M:%S'))
