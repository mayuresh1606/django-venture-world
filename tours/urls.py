from django.urls import path
from . import views


urlpatterns = [
    path('', views.tours, name='tours'),
    path('<package_type>/<package_name>/<int:package_id>',
         views.package_details, name='package_detail'),
    path('services', views.services, name='services'),
    path('contactUs', views.contact_us, name='contact-us'),
    path('terms', views.terms, name='terms'),
    path('indiv-pack', views.indiv_pack, name='indiv-pack'),
    path('<int:package_id>', views.individual_package_detail,
         name='individual_package_detail'),
    path('EducationalTours', views.educational_tours,
         name='educational_tours'),
    path('<package_type>', views.tourDetails, name='tour_details'),
]
