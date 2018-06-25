from django.contrib import admin

# Register your models here.

from api.models import Snippet,Test,Contact,Tag

@admin.register(Snippet)
class SnipAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'code', 'language', 'style')
    list_per_page = 20
    ordering = ('id',)
    list_filter = ('language',)
    search_fields = ('code', 'language', 'style')


class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('age',),
        }]

    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])

