from django.contrib import admin

# Register your models here.
from .models import Finch, GrabbedItem

admin.site.register(Finch)
admin.site.register(GrabbedItem)