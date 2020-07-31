from django.contrib import admin
from bookshop.models import Event, Holiday, Country, User


class EventAdmin(admin.ModelAdmin):
    exclude = ("tmp_duration_field", )


class HolidayAdmin(admin.ModelAdmin):
	list_filter = ["country"]


admin.site.register(Event, EventAdmin)
admin.site.register(Holiday, HolidayAdmin)
admin.site.register(Country)
admin.site.register(User)
