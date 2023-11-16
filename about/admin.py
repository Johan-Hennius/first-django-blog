from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
# Register your models here.
class AboutAdmin(SummernoteModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body')


