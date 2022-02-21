from django.db import models
from django.shortcuts import render
from tours.models import IndividualPackage, Night, Day, PackageType, BannerImage, EducationalTour, GroupSubPackage, ImportantPackage


def index(request):
    imp_pack_names = []

    imp_packages = IndividualPackage.objects.filter(important=True)

    pilgrimage = PackageType.objects.filter(package_type='Pilgrimage')
    adventure_tour = PackageType.objects.filter(package_type='Adventure Tour')

    # pilgrimages = pilgrimage.individualpackage_set.all()
    # adventure_tours = adventure_tour.individualpackage_set.all()

    imp_package_types = ImportantPackage.objects.all()
    for imp_pack in imp_packages:
        imp_pack_name = imp_pack.package_name
        imp_pack_names.append(imp_pack_name)

    packageTypes = PackageType.objects.all()
    all_packages = IndividualPackage.objects.all()
    banner_images = BannerImage.objects.all()

    group_sub_packages = GroupSubPackage.objects.all()

    educational_tours = EducationalTour.objects.all()
    context = {
        'all_packages': all_packages,
        'pack_types': packageTypes,
        'banner_images': banner_images, 'imp_pack_types': imp_package_types, 'imp_packages': imp_packages, 'imp_pack_names': imp_pack_names,
        'educational_tours': educational_tours,
        # 'pilgrimages': pilgrimages, 'adventure_tours': adventure_tours,
        'group_sub_packages': group_sub_packages}

    return render(request, 'tours/index.html', context)
