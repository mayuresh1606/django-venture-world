from django.core.exceptions import ObjectDoesNotExist
from django.db.models.lookups import In
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import IndividualPackage, Day, Night, PackageType
from django.core.mail import send_mail


def tours(request):
    packageTypes = PackageType.objects.all()
    packages = IndividualPackage.objects.all()
    tours_package = []
    for package_type in packageTypes:
        packages_type = package_type.individualpackage_set.all()
        tours_package.append(packages_type)
    for pack in tours_package:
        print(len(tours_package))
        print(len(pack))
        for pac in pack:
            print(pac.package_name)

    context = {'packageTypes': packageTypes,
               'packages': packages, 'tours_packages': tours_package}
    return render(request, 'tours/tours.html', context)


def package_details(request, package_type):
    packages = PackageType.objects.get(package_type=package_type)
    package = packages.individualpackage_set.all()
    list = []
    for pack in package:
        if pack.package_name == 'Himachal':
            list.append(pack)

    context = {'package': list}
    return render(request, 'tours/package_detail.html', context)


def individual_package_detail(request, package_id):
    indiv_package = IndividualPackage.objects.get(pk=package_id)
    context = {'pack': indiv_package}
    return render(request, 'tours/individual_package_detail.html', context)


def tourDetails(request, package_type):
    packagesType = PackageType.objects.get(package_type=package_type)
    tourPackage = packagesType.individualpackage_set.all()
    pack = ''
    for pack_name in package_type:
        pack += pack_name
    context = {'tour_package': tourPackage, 'package_type': pack}
    return render(request, 'tours/tour_details.html', context)


def services(request):
    try:
        packages = PackageType.objects.all()
        context = {'packages': packages}
    except ObjectDoesNotExist:
        packages = None
    return render(request, 'tours/services.html')


def terms(request):
    return render(request, 'tours/terms.html')


def contact_us(request):
    if request.method == 'POST':
        senders_name = request.POST['senders-name']
        senders_email = request.POST['senders-email']
        message = request.POST['message']

        send_mail(senders_name + ' - ' + senders_email, message, senders_email,
                  ['mayureshovhal1606@gmail.com'])

        return render(request, 'tours/contactUs.html', {'senders_name': senders_name})
    else:
        return render(request, 'tours/contactUs.html')


def indiv_pack(request):
    packages = IndividualPackage.objects.all()
    return render(request, 'tours/indiv_pack.html', context={'packages': packages})
