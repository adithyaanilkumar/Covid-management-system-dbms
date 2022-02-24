from django.contrib import admin
from administrator.models import personal_details,id_card,travel_details,health_details,vaccination_details
# Register your models here.

admin.site.register(personal_details)
admin.site.register(id_card)
admin.site.register(travel_details)
admin.site.register(health_details)
admin.site.register(vaccination_details)
