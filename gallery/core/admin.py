from django.contrib import admin
from core.models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description', 'landscape',]
    list_filter = ['landscape', 'date']
    search_fields = ['name', 'description', ]
    readonly_fields = ['date', ]
    fieldsets = [
        ('Details', {
            'classes': ('wide', ),
            'fields': ('name', 'description', 'landscape')
        }),
        ('Image', {
            'fields': ('image', )
        }),
        ('Date', {
            'classes': ('wide', ),
            'fields': ('date', )
        })
    ]

admin.site.register(Image, ImageAdmin)