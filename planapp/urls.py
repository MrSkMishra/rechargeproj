from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^list-plans/$', list_plans, name='list_plans'),
    re_path(r'^initiate-recharge/$', initiate_recharge, name='initiate_recharge'),
]
