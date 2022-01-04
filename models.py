from django.db import models


# Create your models here.
# makemigrations - create changes and store in a file
# migrate - apply pending changes created by makemigrations
class Register(models.Model):
    firstname =  models.CharField(max_length=100)
    lastname =  models.CharField(max_length=100)
    phoneno = models.CharField(max_length=10)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=10)
    usertype =  (
   ('Alumni','Alumni'),
   ('Staff','Staff'),
   ('Students','Students')
)

    usertype = models.CharField(choices=usertype, max_length=122) 
    address = models.CharField(max_length=122)
    address2 = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    state = models.CharField(max_length=122)
    zip = models.CharField(max_length=122)
    college = models.CharField(max_length=122)
    department = models.CharField(max_length=122)
    yop = models.DateField()

    def __str__(self):
        return self.firstname + self.lastname
    





