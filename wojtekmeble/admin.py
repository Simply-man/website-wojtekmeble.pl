from django.contrib import admin

from .models import Pictures


# class PicturesAdmin(admin.ModelAdmin):
#     date_hierarchy = 'pub_date'
#     list_display = ('picture', 'pub_date')


class PicturesAdmin(admin.TabularInline):
    model = Pictures
    fields = ['picture', ]


admin.site.register(Pictures)
