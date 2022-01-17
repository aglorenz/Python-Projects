from django.db import models


# Create your models here.
class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=False, null=False)
    course_number = models.IntegerField(default=0, blank=False, null=False)
    instructor_name = models.CharField(max_length=60, default="")
    duration = models.FloatField(default=0, blank=False, null=False)

    objects = models.Manager()    # object manager

    def __str__(self):
        return self.title


# This is a quick an dirty way to populate a few rows in the database, however
# Make sure the table exists before adding these rows (run makemigrations, migrate)
# otherwise you'll get error:  "no such table: classApp_djangoclasses"
# After adding these rows, just run migrate and the rows will be added
# The rows will be added twice each time you start the server as well.
class1 = djangoClasses(title="Cooking", course_number=101, instructor_name="Dr Fredrickson", duration=1.5)
class1.save()
class2 = djangoClasses(title="Swimming", course_number=102, instructor_name="Mrs Shipley", duration=4.0)
class2.save()
class3 = djangoClasses(title="Eating", course_number=103, instructor_name="Mr Broth", duration=2.5)
class3.save()

