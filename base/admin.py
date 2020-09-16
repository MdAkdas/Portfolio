from django.contrib import admin

# Register your models here.
from .models import Tag, Post

admin.site.register(Post)
admin.site.register(Tag)