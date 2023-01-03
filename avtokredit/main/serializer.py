from rest_framework.serializers import ModelSerializer
from .models import *


class CreditSerializer(ModelSerializer):
    class Meta:
        model = Credit
        fields = '__all__'

class UserSerialier(ModelSerializer):
    class Meta:
        model = User