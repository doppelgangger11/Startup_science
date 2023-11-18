import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TeachersAddInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='static/profile/avatars/', null=True, blank=True)
    degree = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    orcid =  models.CharField(max_length=100, default=None)
    Scopus_ID = models.CharField(max_length=100, default=None)
    Web_of_Science_ResearcherID = models.CharField(max_length=100, default=None)
    scientific_interests = models.CharField(max_length=500, default=None)

class Table(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='table')
    author_name = models.CharField( max_length=100)
    patent = models.CharField( max_length=100)
    year = models.CharField( max_length=100)
    title = models.CharField( max_length=100)
    date = models.DateField(default=datetime.date.today)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
    
class Table23(models.Model):
     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='table23')
     subject = models.CharField(max_length=100)
     name_of_partner = models.CharField(max_length=100)
     date_of_contract = models.DateField() 
     start_date = models.DateField()
     #start_date = models.CharField(max_length=100)
     end_date = models.DateField()
     availability = models.CharField(max_length=100)
     date = models.DateField(default=datetime.date.today)

     def publish(self):
        self.save()

     def __str__(self):
        return self.availability
     
class Table26(models.Model):
     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='table26')
     organisation = models.CharField(max_length=100)
     subject_of_contract = models.CharField(max_length=100)
     directon_of_speciality = models.CharField(max_length=40)
     date_of_conclusion_of_the_contract = models.DateField()
     terms_of_the_contract = models.CharField(max_length=40)
     date = models.DateField(default=datetime.date.today)

     def publish(self):
        self.save()

     def __str__(self):
        return self.terms_of_the_contract
     
# Table(№) -> user.tables.all()
# change nomer of table in author.related_name !!!
