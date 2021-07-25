from django.db import models


class PackageType(models.Model):
    package_type = models.CharField(max_length=255)
    image = models.ImageField()

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


class IndividualPackage(models.Model):
    package_name = models.CharField(max_length=255)
    image = models.ImageField()
    package_type = models.ForeignKey(PackageType, on_delete=models.CASCADE)
    days = models.ForeignKey(Day, on_delete=models.CASCADE)
    nights = models.ForeignKey(Night, on_delete=models.CASCADE)
    starts_from = models.IntegerField(default=0)
    destination_1 = models.CharField(max_length=255, null=True, blank=True)
    destination_1_nights = models.IntegerField(default=1)
    destination_2 = models.CharField(max_length=255, null=True, blank=True, default=False)
    destination_2_nights = models.IntegerField(default=0)
    destination_3 = models.CharField(max_length=255, default=False)
    destination_3_nights = models.IntegerField(default=0)

    def __str__(self):
        return self.package_name

    # def __str__(self):
    #     return self.package_type
