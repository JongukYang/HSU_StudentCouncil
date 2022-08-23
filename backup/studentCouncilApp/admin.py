from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','user','user_id','title','body','hits','image','video')
admin.site.register(Post, PostAdmin)