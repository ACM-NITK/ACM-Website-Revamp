from django.db import models
from acm.models import SIG

class SMP(models.Model):
 sig_id = models.ForeignKey(SIG, on_delete=models.CASCADE)
 name = models.CharField(max_length=20000)
 mentors = models.CharField(max_length=20000)
 overview = models.CharField(max_length=20000)
 platform_of_tutoring = models.CharField(max_length=10000)
 def __str__(self):
        return self.name

class SMP_des(models.Model):
 smp_id = models.ForeignKey(SMP, on_delete=models.CASCADE)
 sub_heading = models.CharField(max_length=20000)
 sub_des = models.CharField(max_length=10000) 
 def __str__(self):
        return self.sub_heading

