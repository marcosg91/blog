from django.contrib import admin
from .models import *



class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'slug', 'created_at')
	search_fields = ('post', 'created_at')
	prepopulated_fields = {'slug': ('name',),}	

admin.site.register(Category, CategoryAdmin)



@admin.action(description='Mark selected stories as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='publish')

@admin.action(description='Mark selected stories as draft')
def make_draft(modeladmin, request, queryset):
    queryset.update(status='draft')

class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'slug', 'author', 'category', 'created_on', 'status')
	list_filter = ('status',)
	search_fields = ('post', 'category')
	prepopulated_fields = {'slug': ('title',),}
	actions = [make_published, make_draft]

admin.site.register(Publicación, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'author', 'created_on', 'active', 'post')
	list_filter = ('active', 'created_on')
	search_fields = ('author', 'created_on', 'active', 'content')

admin.site.register(Comment, CommentAdmin)
