from django.db import models

class MobileRechargePlan(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    validity = models.IntegerField()
    network = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    plan = models.ForeignKey(MobileRechargePlan, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    network = models.CharField(max_length=255)

    def __str__(self):
        return self.plan
