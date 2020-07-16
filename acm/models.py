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
 display_picture = models.ImageField(upload_to='uploads/projects', null=True)
 duration_in_months = models.IntegerField(null=True)
 mentors = models.TextField()
 members = models.TextField()
 introduction = models.TextField()
 method = models.TextField()
 results = models.TextField()
 obstacles = models.TextField()
 conclusion = models.TextField()
 future_work = models.TextField()
 references = models.TextField()

 def __str__(self):
        return self.name

class ProjectPictures(models.Model):
 project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
 picture = models.ImageField(upload_to = 'uploads/projects', null=True)

class Special_people(models.Model):
 name = models.CharField(max_length=30)  #As only first name is mentioned
 post = models.CharField(max_length=25)
 fb_link = models.CharField(max_length=500)
 linkedin_link = models.CharField(max_length=500)
 image_path = models.CharField(max_length=200)
 def __str__(self):
        return self.name


