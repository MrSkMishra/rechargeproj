from rest_framework import serializers
from .models import MobileRechargePlan, Transaction

class MobileRechargePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileRechargePlan
        fields = ('id', 'name', 'price', 'validity', 'network')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'plan', 'phone_number', 'amount', 'status')
