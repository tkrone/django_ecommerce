from profiles.models import Profile
from django.contrib import admin

# Register your models here.
from .models import Product

admin.site.register(Product)