from django.contrib import admin

# Register your models here.
from myblog.models import Post
from myblog.models import Category

admin.site.register(Post)

admin.site.register(Category)