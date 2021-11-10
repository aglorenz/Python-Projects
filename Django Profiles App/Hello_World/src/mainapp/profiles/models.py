from django.db import models

PREFIX_CHOICES = {
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Ms', 'Ms'),
    ('Dr', 'Dr'),
    ('Prince', 'Prince'),
    ('Princess', 'Princess'),
    ('Rev', 'Rev'),
}


class Profile(models.Model):
    prefix = models.CharField(max_length=15, choices=PREFIX_CHOICES)
    first_name = models.CharField(max_length=60, default="", blank=False, null=False)
    last_name = models.CharField(max_length=60, default="", blank=False, null=False)
    email = models.CharField(max_length=60, default="", blank=False, null=False)
    phone = models.CharField(max_length=60, default="", blank=False, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.first_name

# two entries get inserted into the table when you run python manage.py runserver
# but if you run python manage.py runserver --noreload you only get 1 row added
# see https://stackoverflow.com/questions/2110545/why-is-init-module-in-django-project-loaded-twice
# obj1 = Profile(prefix="Mr",first_name="George",last_name="blog",email='andy@andy.com',phone="555-555-5555")
# obj1.save()