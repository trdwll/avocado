from django.contrib import admin
from . models import Post

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted', 'author']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'category', 'author', 'sub_heading', 'body']

    def save_model(self, request, obj, form, change):
    	obj.author = request.user.get_username()
    	super(BlogAdmin, self).save_model(request, obj, form, change)

admin.site.register(Post, BlogAdmin)