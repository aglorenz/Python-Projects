from django.contrib import admin

# Register your models here.
from .models import djangoClasses  # import our new model

admin.site.register(djangoClasses)  # and register it here
