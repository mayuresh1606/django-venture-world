from django.db import models
from django.shortcuts import render
from tours.models import IndividualPackage, Night, Day, PackageType


def index(request):
    type = 'Himachal'
    packages = IndividualPackage.objects.all()
    package = packages.filter(package_name=type)
    packageTypes = PackageType.objects.all()
    all_packages = IndividualPackage.objects.all()

    # all_packages.filter(package_type = )
    context = {'package': package,
               'all_packages': all_packages,
               'packages': packages,
               'pack_types': packageTypes}
    return render(request, 'tours/index.html', context)
