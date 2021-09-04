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

obj1 = Profile(prefix="Mr",first_name="Levi",last_name="blog",email='andy@andy.com',phone="555-555-5555")
obj1.save()