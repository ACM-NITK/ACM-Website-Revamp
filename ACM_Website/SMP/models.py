from djongo import models


class Description(models.Model):
    description = models.CharField(max_length=1000)
    objects = models.DjongoManager()

    def __str__(self):
        return self.description


class WeeklyPlan(models.Model):
    week_description = models.ArrayModelField(
        model_container=Description, default=[])
    objects = models.DjongoManager()


class SMP(models.Model):
    sig_id = models.IntegerField(default=1)
    name = models.CharField(max_length=200)
    mentors = models.CharField(max_length=200)
    overview = models.CharField(max_length=2000)
    platform_of_tutoring = models.CharField(max_length=1000)
    exercises = models.ArrayModelField(model_container=Description, default=[])
    prerequisites = models.ArrayModelField(
        model_container=Description, default=[])
    course_content = models.ArrayModelField(
        model_container=Description, default=[])
    weekly_plan = models.ArrayModelField(
        model_container=WeeklyPlan, default=[])

    objects = models.DjongoManager()

    def __str__(self):
        return self.name
