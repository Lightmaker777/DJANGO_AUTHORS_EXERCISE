from django.contrib import admin
from .models import Author,Publisher,Books,User
# Register your models here.
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(User)
admin.site.register(Books)
