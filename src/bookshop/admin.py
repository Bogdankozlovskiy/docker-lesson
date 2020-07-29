from django.contrib import admin
from bookshop.models import Event, Holiday


class EventAdmin(admin.ModelAdmin):
    exclude = ("tmp_duration_field", )


admin.site.register(Event, EventAdmin)
admin.site.register(Holiday)
