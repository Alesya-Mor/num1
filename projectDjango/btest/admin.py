from django.contrib import admin
from .models import *

class BbAdmin(admin.ModelAdmin):
  list_display = ('title', 'content', 'price', 'published')
  list_display_links = ('title', 'content')
  search_fields = ('title', 'content', 'price', 'published',)

admin.site.register(Bb, BbAdmin)

class RubricAdmin(admin.ModelAdmin):
   list_display = ('name',)

admin.site.register(Rubric,RubricAdmin )

admin.site.register(Exponat)
admin.site.register(Collection)