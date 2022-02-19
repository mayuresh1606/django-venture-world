from django.contrib import admin
from .models import IndividualPackage, PackageType, Night, Day, BannerImage, EducationalTour, GroupSubPackage, LeftImage, RightImage, ImportantPackage, CurrentTours


class PackageTypeAdmin(admin.ModelAdmin):
    list_display = ['package_type']


class IndividualPackageAdmin(admin.ModelAdmin):
    list_display = ['package_name', 'package_type']


class CurrentToursAdmin(admin.ModelAdmin):
    list_display = ['name', "comfort_name"]


class DaysAdmin(admin.ModelAdmin):
    list_display = ['day']


class NightsAdmin(admin.ModelAdmin):
    list_display = ['night']


class GroupSubPackageAdmin(admin.ModelAdmin):
    list_display = ['group_sub_package']


class EducationalTourAdmin(admin.ModelAdmin):
    list_display = ['destination']


class LeftImageAdmin(admin.ModelAdmin):
    list_display = ['image']


class RightImageAdmin(admin.ModelAdmin):
    list_display = ['image']


class ImportantPackageAdmin(admin.ModelAdmin):
    list_display = ['important_package']


admin.site.register(IndividualPackage, IndividualPackageAdmin)
admin.site.register(CurrentTours, CurrentToursAdmin)
admin.site.register(PackageType, PackageTypeAdmin)
admin.site.register(Day, DaysAdmin)
admin.site.register(Night, NightsAdmin)
admin.site.register(BannerImage)
admin.site.register(EducationalTour, EducationalTourAdmin)
admin.site.register(GroupSubPackage, GroupSubPackageAdmin)
admin.site.register(LeftImage, LeftImageAdmin)
admin.site.register(RightImage, RightImageAdmin)
admin.site.register(ImportantPackage, ImportantPackageAdmin)
