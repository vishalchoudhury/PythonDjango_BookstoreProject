from django.contrib import admin
from .models import book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
	list_display = ("title","author","price","stock")

admin.site.register(book,BookAdmin)