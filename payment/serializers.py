from rest_framework import serializers
from . import models


class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.CheckOut
        fields = '__all__'