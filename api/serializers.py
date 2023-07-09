from rest_framework import serializers


class PaymentResponseSerializer(serializers.Serializer):
    tran_ref = serializers.CharField()
    tran_type = serializers.CharField()
    cart_id = serializers.CharField()
    cart_description = serializers.CharField()
    cart_currency = serializers.CharField()
    cart_amount = serializers.CharField()
    tran_currency = serializers.CharField(required=False, allow_blank=True)
    tran_total = serializers.CharField()
    callback = serializers.CharField()
    redirect_url = serializers.CharField()
    return_url = serializers.URLField(source='return'),
    trace = serializers.CharField()
    serviceId = serializers.IntegerField()
    profileId = serializers.IntegerField()
    merchantId = serializers.IntegerField()

    class Meta:
        fields = (
            'tran_ref', 'tran_type', 'cart_id', 'cart_description', 'cart_currency', 'cart_amount', 'tran_currency',
            'tran_total', 'callback', 'redirect_url', 'return_url', 'trace', 'serviceId', 'profileId', 'merchantId')
