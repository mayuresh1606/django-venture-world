from django.contrib import admin
from .models import IndividualPackage, PackageType, Night, Day


class PackageTypeAdmin(admin.ModelAdmin):
    list_display = ['package_type']


class IndividualPackageAdmin(admin.ModelAdmin):
    list_display = ['package_name', 'package_type']


class DaysAdmin(admin.ModelAdmin):
    list_display = ['day']


class NightsAdmin(admin.ModelAdmin):
    list_display = ['night']


admin.site.register(IndividualPackage, IndividualPackageAdmin)
admin.site.register(PackageType, PackageTypeAdmin)
admin.site.register(Day, DaysAdmin)
admin.site.register(Night, NightsAdmin)
