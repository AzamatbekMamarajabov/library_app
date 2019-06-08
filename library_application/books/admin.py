from django.contrib import admin

from .models import Books, BooksInformation


class BooksInformationInline(admin.TabularInline):
    model = BooksInformation
    extra =0    


class BooksAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['is_available'], 'classes': ['collapse']}),
    ]
    inlines = [BooksInformationInline]

admin.site.register(Books, BooksAdmin)
