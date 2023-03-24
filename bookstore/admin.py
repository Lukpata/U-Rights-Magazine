from django.contrib import admin
from .models import AuthorProfile,Book,Order


admin.site.register(AuthorProfile)
admin.site.register(Book)
admin.site.register(Order)


