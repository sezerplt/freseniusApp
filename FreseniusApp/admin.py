from django.contrib import admin
from .models import WorkTime,WorkUser,WorkDate
# Register your models here.


admin.AdminSite.site_header="Fresenius Admin"
admin.AdminSite.site_title="FreseniusApp Admin"
admin.site.register(WorkTime)
admin.site.register(WorkUser)
admin.site.register(WorkDate)