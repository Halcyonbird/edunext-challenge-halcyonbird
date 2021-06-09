# -*- coding: utf-8 -*-
"""
Views for customerdataapi.
"""
from __future__ import absolute_import, unicode_literals
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import  APIView
from rest_framework.decorators import  api_view
from customerdataapi.models import CustomerData
from customerdataapi.serializers import CustomerDataSerializer, CustomerPlanSerializer
from datetime import datetime  
## Changes: add required libraries like datetime to saved the date fields with the server date ##

class CustomerDataViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving CustomerData.
    """

    queryset = CustomerData.objects.all()
    serializer_class = CustomerDataSerializer
    permission_classes = (permissions.AllowAny,)



## Changes: add the variable Disabled_Features that load a json file that contains the features in mode disable(false) ##
## Load the Customer model and change the SUBSCRIPTION field to 'free' ##
## save the customer changes without serializer, the serializar only is used to load the new customer data ##
@api_view(['GET'])
def downgrade(request,pk):
    DISABLE_FEATURES = {
        "CERTIFICATES_INSTRUCTOR_GENERATION": False,
        "INSTRUCTOR_BACKGROUND_TASKS": False,
        "ENABLE_COURSEWARE_SEARCH": False,
        "ENABLE_COURSE_DISCOVERY": False,
        "ENABLE_DASHBOARD_SEARCH": False,
        "ENABLE_EDXNOTES": False
    }

    if request.method == "GET":
        customer = CustomerData.objects.get(id=pk)
        customer.SUBSCRIPTION = 'free'
        customer.ENABLED_FEATURES = DISABLE_FEATURES
        customer.DOWNGRADE_DATE = datetime.now()
        customer.save()
        customer_serializer = CustomerPlanSerializer(customer)
        return Response(customer_serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(customer_serializer.data, status=status.HTTP_404_NOT_FOUND)


## Changes: create upgrade function ##
## save the customer changes witht serializer, the serializar is used to save the new customer data through json data ##
@api_view(['GET','PUT'])
def upgrade(request,pk):
    customer = CustomerData.objects.get(id=pk)
    customer_serializer = CustomerPlanSerializer(customer)

    if request.method == "PUT":
        customer = CustomerData.objects.get(id=pk)
        customer.UPGRADE_DATE = datetime.now()
        customer_serializer = CustomerPlanSerializer(customer,data=request.data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return Response(customer_serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(customer_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response(customer_serializer.data,status = status.HTTP_400_BAD_REQUEST)






