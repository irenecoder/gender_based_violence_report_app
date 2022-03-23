from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=10)
    email_address = models.EmailField()
    date_created= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Registered Users'
        verbose_name_plural = 'Registered Users'

    def __str__(self):
        return 'User {} created this account on {}'.format(self.name, self.date_created.strftime('%a %dth-%m-%Y %H:%M:%S'))
        