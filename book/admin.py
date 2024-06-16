from __future__ import unicode_literals

from django.contrib import admin

from .models import Book, Assignment

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name","author"]}),
        ("Details", {"fields": ["publish_date","price","quantity"], "classes": ["collapse"]}),
    ]
    list_display = ["name", "author", "publish_date","price","quantity"]
    list_filter = ["publish_date"]
    search_fields = ["name"]

admin.site.register(Book, BookAdmin)

class AssignmentAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {"fields": ["name","author"]}),
    #     ("Details", {"fields": ["publish_date","price","quantity"], "classes": ["collapse"]}),
    # ]
    list_display = ["roll_id", "book_id", "assigned_on","submitted_on","is_active"]
    list_filter = ["roll_id","book_id"]
    search_fields = ["roll_id"]

admin.site.register(Assignment,AssignmentAdmin)

