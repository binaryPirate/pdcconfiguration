from django.contrib import admin

# Register your models here.
from .models import configuration, post, srcdest

admin.site.register(configuration)
admin.site.register(post)
admin.site.register(srcdest)