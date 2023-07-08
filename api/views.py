from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import uuid
import httpx
import random


@api_view(['POST'])
@permission_classes([AllowAny])
def payment_request(request):
    # cart_amount = request.data.get('cart_amount')
    # currency = request.data.get('currency')
    # coach_name = request.data.get('coach_name')
    # plan_title = request.data.get('plan_title')
    #
    # if not all([cart_amount, currency, coach_name, plan_title]):
    #     return Response({'error': 'Please provide all required fields'})

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
        "cart_currency": "EGP",
        "cart_amount": 10,
        "callback": "https://bodyforge.site/index",
        "return": "https://bodyforge.site/pricing",
    }

    response = httpx.post(url, headers=headers, json=data)

    return Response(response.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def ai_payment_request(request):
    cart_amount = request.data.get('cart_amount')
    currency = request.data.get('currency')
    coach_name = request.data.get('coach_name')
    plan_title = request.data.get('plan_title')

    if not all([cart_amount, currency, coach_name, plan_title]):
        return Response({'error': 'Please provide all required fields'})

    random_number = random.randint(10 ** 16, 10 ** 17 - 1)
    # Obtain CSRF token
    response = httpx.get('https://bodyforge.site/api-auth/csrf/')
    csrf_token = response.cookies.get('csrftoken')

    # Send request with CSRF token
    response = httpx.post(
        'https://secure-egypt.paytabs.com/payment/request',
        headers={
            'X-CSRFToken': csrf_token,
            "authorization": "STJNBZMH29-J6M2KJNNWH-GKNGW9ZTHW",
            "content-type": "application/json",
        },
        json={
            "profile_id": 123108,
            "tran_type": "sale",
            "tran_class": "ecom",
            "cart_id": str(uuid.uuid4()),
            "cart_description": f"Order: {random_number} \n Plan: {plan_title}\n Coach: {coach_name}",
            "cart_currency": currency,
            "cart_amount": cart_amount,
            "callback": "https://bodyforge.site/index",
            "return": "https://bodyforge.site/pricing",
        }
    )

    return Response(response.json())
