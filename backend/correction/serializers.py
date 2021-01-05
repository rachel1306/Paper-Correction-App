from rest_framework import serializers
from .models import Correction

class CorrectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Correction
        fields=('url','code','name')