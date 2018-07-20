from regions.models import CountyModel, ConstituencyModel, WardModel
from rest_framework import serializers

class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardModel
        fields = ('id', 'name', 'date_created', )
        ordering = ('date_created',)

class ConstituencySerializer(serializers.ModelSerializer):
    wards = WardSerializer(many=True, read_only=True)
    class Meta:
        model = ConstituencyModel
        fields = ('id', 'name', 'date_created',  'wards')
        ordering = ('date_created',)
    
class CountySerializer(serializers.ModelSerializer):
    constituencies = ConstituencySerializer(many=True, read_only=True)
    class Meta:
        model = CountyModel
        fields = ('id', 'name', 'date_created', 'constituencies')
        ordering = ('date_created',)


