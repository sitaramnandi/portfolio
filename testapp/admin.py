from django.contrib import admin
from testapp.models import contactus
# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display=["name","email","subject","message"]
admin.site.register(contactus,contactusAdmin)
