from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class SIG(models.Model):
 name = models.CharField(max_length=200)
 image = models.ImageField(upload_to='uploads/sigs', blank=True, null=True, validators=[
     FileExtensionValidator(['jpg', 'jpeg', 'png', ])])
 mission_statement = models.TextField()
 vision_statement = models.TextField()

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
 display_picture = models.ImageField(upload_to='uploads/projects', blank=True, null=True, validators=[
                                     FileExtensionValidator(['jpg', 'jpeg', 'png', ])])
 duration_in_months = models.IntegerField(blank=True)
 mentors = models.TextField(blank=True)
 members = models.TextField(blank=True)
 introduction = models.TextField(blank=True)
 method = models.TextField(blank=True)
 results = models.TextField(blank=True)
 obstacles = models.TextField(blank=True)
 conclusion = models.TextField(blank=True)
 future_work = models.TextField(blank=True)
 references = models.TextField(blank=True)
 knowledge = models.TextField(blank=True)
 meet_link = models.CharField(max_length=500, blank=True)
 year = models.IntegerField()

 def __str__(self):
        return self.name

class Proposals(models.Model):
    sig_id = models.ForeignKey(SIG, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    duration_in_months = models.IntegerField(blank=True)
    mentors = models.TextField(blank=True)
    members = models.TextField(blank=True)
    introduction = models.TextField(blank=True)
    method = models.TextField(blank=True)
    existing_work = models.TextField(blank=True)

    application = models.TextField(blank=True)
    references = models.TextField(blank=True)
    def __str__(self):
        return self.name


class ProjectPictures(models.Model):
 project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
 picture = models.ImageField(upload_to='uploads/projects', blank=True, null=True,
                             validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', ])])
 title = models.TextField(blank=True)


class Special_people(models.Model):
 name = models.CharField(max_length=30)  # As only first name is mentioned
 post = models.CharField(max_length=25)
 fb_link = models.CharField(max_length=500)
 linkedin_link = models.CharField(max_length=500)
 image_path = models.CharField(max_length=200)

 def __str__(self):
        return self.name
