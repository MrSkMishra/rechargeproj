from .serializers import MobileRechargePlanSerializer, TransactionSerializer
from django.http import JsonResponse
from .models import *

def list_plans(request):
    
    plans = MobileRechargePlan.objects.all()
    serializer = MobileRechargePlanSerializer(plans, many=True)
    return JsonResponse({"plans": serializer.data})

def initiate_recharge(request):
    
    plans = Transaction.objects.all()
    serializer = TransactionSerializer(plans,many=True)
    return JsonResponse({"Success Your Recharge Is being Successfull":serializer.data})

