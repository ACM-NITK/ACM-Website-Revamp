from django.db import models

# Create your models here.


class SIG(models.Model):
 name = models.CharField(max_length=200)
 def __str__(self):
        return self.name


class Events(models.Model):
 sig_id = models.ForeignKey(SIG, on_delete=models.CASCADE)
 name = models.CharField(max_length=200)
 description = models.CharField(max_length=5000)
 def __str__(self):
        return self.name

class Projects(models.Model):
 sig_id = models.ForeignKey(SIG, on_delete=models.CASCADE)
 name = models.CharField(max_length=200)
 description = models.CharField(max_length=5000)
 report_link = models.CharField(max_length=500,null=True)
 poster_link = models.CharField(max_length=500,null=True)
 def __str__(self):
        return self.name

class Special_people(models.Model):
 name = models.CharField(max_length=30)  #As only first name is mentioned
 post = models.CharField(max_length=25)
 fb_link = models.CharField(max_length=500)
 linkedin_link = models.CharField(max_length=500)
 image_path = models.CharField(max_length=200)
 def __str__(self):
        return self.name


