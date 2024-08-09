from rest_framework import serializers
from .models import QRCodeModel


class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCodeModel
        fields = ['id', 'name', 'link']