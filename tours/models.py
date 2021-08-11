from django.db import models


class PackageType(models.Model):
    package_type = models.CharField(max_length=255)
    image = models.ImageField()
    left_image_1 = models.ImageField()
    left_image_2 = models.ImageField()
    left_image_3 = models.ImageField()
    left_image_4 = models.ImageField()
    left_image_5 = models.ImageField()
    left_image_6 = models.ImageField()
    right_image_1 = models.ImageField()
    right_image_2 = models.ImageField()
    right_image_3 = models.ImageField()
    right_image_4 = models.ImageField()
    right_image_5 = models.ImageField()
    right_image_6 = models.ImageField()

    def __str__(self):
        return self.package_type


class Night(models.Model):
    night = models.IntegerField()

    def __str__(self):
        return str(self.night)


class Day(models.Model):
    day = models.IntegerField()

    def __str__(self):
        return str(self.day)


class State(models.Model):
    state = models.CharField(max_length=255)

    def __str__(self):
        return self.state


class BannerImage(models.Model):
    image = models.ImageField()


class GroupSubPackage(models.Model):
    group_sub_package = models.CharField(max_length=255, default=False)

    def __str__(self):
        return self.group_sub_package


class ImportantPackage(models.Model):
    important_package = models.CharField(max_length=255, default=False)

    def __str__(self):
        return self.important_package


class IndividualPackage(models.Model):
    important = models.BooleanField(default=False)
    important_package_type = models.ForeignKey(
        ImportantPackage, on_delete=models.CASCADE, null=True, blank=True)
    package_name = models.CharField(max_length=255)
    image = models.ImageField()
    package_type = models.ForeignKey(
        PackageType, on_delete=models.CASCADE)
    group_packages = models.ForeignKey(
        GroupSubPackage, on_delete=models.CASCADE, null=True, blank=True)
    days = models.ForeignKey(Day, on_delete=models.CASCADE)
    nights = models.ForeignKey(Night, on_delete=models.CASCADE)
    starts_from = models.IntegerField(default=0)
    destination_1 = models.CharField(max_length=255, null=True, blank=True)
    destination_1_nights = models.IntegerField(default=1)
    destination_2 = models.CharField(
        max_length=255, null=True, blank=True, default=False)
    destination_2_nights = models.IntegerField(default=0)
    destination_3 = models.CharField(max_length=255, default=False)
    destination_3_nights = models.IntegerField(default=0)

    itinerary_date_1 = models.CharField(max_length=24, default=False)
    itinerary_description_1 = models.CharField(max_length=1024, default=False)
    itinerary_date_2 = models.CharField(max_length=24, default=False)
    itinerary_description_2 = models.CharField(max_length=1024, default=False)
    itinerary_date_3 = models.CharField(max_length=24, default=False)
    itinerary_description_3 = models.CharField(max_length=1024, default=False)
    itinerary_date_4 = models.CharField(max_length=24, default=False)
    itinerary_description_4 = models.CharField(max_length=1024, default=False)
    itinerary_date_5 = models.CharField(max_length=24, default=False)
    itinerary_description_5 = models.CharField(max_length=1024, default=False)
    itinerary_date_6 = models.CharField(max_length=24, default=False)
    itinerary_description_6 = models.CharField(max_length=1024, default=False)

    def __str__(self):
        return self.package_name


class EducationalTour(models.Model):
    destination = models.CharField(max_length=255)
    nights = models.IntegerField(default=0)
    days = models.IntegerField(default=0)
    places_of_visit = models.CharField(max_length=255)
    lux_bus_non_ac = models.IntegerField(default=0)
    lux_bus_ac = models.IntegerField(default=0)
    out_of_state = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    transportation_1 = models.CharField(max_length=255, default=False)
    transportation_1_nights = models.IntegerField(default=1)
    transportation_1_days = models.IntegerField(default=2)
    transportation_1_cost_non_ac = models.IntegerField(default=0)
    transportation_1_cost_ac = models.IntegerField(default=0)

    transportation_2 = models.CharField(max_length=255, default=False)
    transportation_2_nights = models.IntegerField(default=1)
    transportation_2_days = models.IntegerField(default=2)
    transportation_2_cost_non_ac = models.IntegerField(default=0)
    transportation_2_cost_ac = models.IntegerField(default=0)

    transportation_3 = models.CharField(max_length=255, default=False)
    transportation_3_nights = models.IntegerField(default=1)
    transportation_3_days = models.IntegerField(default=2)
    transportation_3_cost_non_ac = models.IntegerField(default=0)
    transportation_3_cost_ac = models.IntegerField(default=0)


class LeftImage(models.Model):
    image_number = models.IntegerField(default=0)
    image = models.ImageField()


class RightImage(models.Model):
    image_number = models.IntegerField(default=0)
    image = models.ImageField()
