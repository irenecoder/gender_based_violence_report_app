from django.db import models
# from useraccounts.models import Users

class Report(models.Model):
    # crimeid = models.ForeignKey(Users, on_delete=models.CASCADE)
    crime_location = models.CharField(max_length=100)
    type_of_crime = models.CharField(max_length=100)
    date_of_crime = models.CharField(max_length=100)
    crime_description = models.CharField(max_length=100)
    crime_date = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     verbose_name = 'Reported Crimes'
    #     verbose_name_plural = verbose_name

    def __str__(self):
        return 'Crime {} was reported on {}'.format(self.type_of_crime, self.crime_date.strftime('%a %dth-%m-%Y %H:%M:%S'))
