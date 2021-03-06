from asyncio import current_task
from threading import currentThread
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import ImportantPackage, GroupSubPackage, IndividualPackage, Day, Night, PackageType, EducationalTour, LeftImage, RightImage, CurrentTour
from django.core.mail import send_mail


def tours(request):
    packageTypes = PackageType.objects.all()
    packages = IndividualPackage.objects.all()
    tours_package = []
    for package_type in packageTypes:
        packages_type = package_type.individualpackage_set.all()
        tours_package.append(packages_type)

    context = {'packageTypes': packageTypes,
               'packages': packages, 'tours_packages': tours_package}
    return render(request, 'tours/tours.html', context)


# get page according to package name

def package_name_details(request, package_type):

    context = {"package_type": package_type}
    if (package_type == "Himachal"):
        return render(request, "tours/package_name.html", context)
    elif (package_type == "Karnataka"):
        return render(request, "tours/package_name_karnataka.html", context)


def package_details(request, package_type, package_name, package_id):
    packages = IndividualPackage.objects.filter(pk=package_id)

    adventure = False
    if package_type == 'Adventure Tour':
        adventure = True
    context = {'package': packages, 'adventure': adventure,
               'package_name': package_name}
    return render(request, 'tours/package_detail.html', context)


def individual_package_detail(request, package_id):
    indiv_package = IndividualPackage.objects.get(pk=package_id)
    context = {'pack': indiv_package}
    return render(request, 'tours/individual_package_detail.html', context)


def tourDetails(request, package_type):
    packagesType = PackageType.objects.get(package_type=package_type)
    tourPackage = packagesType.individualpackage_set.all()

    group_packages = GroupSubPackage.objects.all()
    packageType = package_type

    pack = ''
    for pack_name in package_type:
        pack += pack_name
    context = {'tour_package': tourPackage,
               'package_types': packagesType, 'group_packages': group_packages, 'package_type': packageType}
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


def educational_tours(request):
    educational_tours = EducationalTour.objects.all()

    left_images = LeftImage.objects.all()
    right_images = RightImage.objects.all()

    context = {'educational_tours': educational_tours,
               'left_images': left_images, 'right_images': right_images}
    return render(request, 'tours/educational_tours.html', context)


# Important Current tours
def current_tours(request, tour_name):
    current_tours = CurrentTour.objects.filter(name=tour_name)
    current_tours = current_tours.order_by("tour_number")
    print("currenttours called")

    context = {"tours": current_tours, "tour_name": tour_name}

    return render(request, "tours/current_tours.html", context)
