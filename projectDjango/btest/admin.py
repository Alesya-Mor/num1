from django.contrib import admin
from .models import Bb

class BbAdmin(admin.ModelAdmin):
  list_display = ('title', 'content', 'price', 'published')
  list_display_links = ('title', 'content')
  search_fields = ('title', 'content', 'price', 'published',)

admin.site.register(Bb, BbAdmin)
from .models import Rubric
...
admin.site.register(Rubric)
list_display = ('title', 'content', 'price', 'published',)