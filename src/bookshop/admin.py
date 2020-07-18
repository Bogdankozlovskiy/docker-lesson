from django.contrib import admin
from bookshop.models import Event


class EventAdmin(admin.ModelAdmin):
    # fields = ("title", "date_start", "date_stop", "reminder")
    exclude = ("tmp_duration_field", )


admin.site.register(Event, EventAdmin)
