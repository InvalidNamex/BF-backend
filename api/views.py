from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import uuid
import httpx
import random
from .serializers import *


@api_view(['POST'])
@permission_classes([AllowAny])
def payment_request(request):
    currency = request.data.get('currency', '').upper()
    random_number = random.randint(10 ** 16, 10 ** 17 - 1)
    url = "https://secure-egypt.paytabs.com/payment/request"
    headers = {
        "authorization": "STJNBZMH29-J6M2KJNNWH-GKNGW9ZTHW",
        "content-type": "application/json",
    }
    data = {
        "profile_id": 123108,
        "tran_type": "sale",
        "tran_class": "ecom",
        "cart_id": str(uuid.uuid4()),
        "cart_description": f"Order: {random_number} \n Plan: Bronze\n Coach: Ahmed",
        "cart_currency": currency,
        "cart_amount": 10,
        "callback": "https://bodyforge.site/index",
        "return": "https://bodyforge.site/pricing",
    }

    response = httpx.post(url, headers=headers, json=data)

    serializer = PaymentResponseSerializer(data=response.json())
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    data['currency'] = currency
    return Response(data)

