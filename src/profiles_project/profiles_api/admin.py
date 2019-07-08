from django.contrib import admin


# from current location import models
from . import models


# Register your models here.
admin.site.register(models.UserProfile)
