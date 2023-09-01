from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(UserLogin)
class UserLoginAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'firstname', 'lastname', 'password')

@admin.register(Contact)
class AddContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'userid', 'firstname', 'lastname',  'relationship', 'email', 'address', 'phone')