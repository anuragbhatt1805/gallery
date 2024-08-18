from django.contrib import admin
from core.models import Image
from cloudinary.uploader import destroy

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

    def delete_model(self, request, obj=None):
        if obj and obj.image:
            # Extract the public ID from the image URL
            public_id = obj.image.name.split('/')[-1].split('.')[0]
            # Destroy the image from Cloudinary
            destroy(public_id)
        return super().delete_model(request, obj)

admin.site.register(Image, ImageAdmin)
