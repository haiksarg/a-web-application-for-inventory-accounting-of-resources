from rest_framework import serializers

from .models import Resources


class ResourcesSerializer(serializers.ModelSerializer):
    cost = serializers.SerializerMethodField()

    class Meta:
        model = Resources
        fields = ('title', 'id', 'amount', 'unit', 'price', 'cost', 'date')

    def get_cost(self, obj):
        return obj.amount * obj.price

    def validate(self, data):
        if data['amount'] < 0 or data['price'] < 0:
            raise serializers.ValidationError()
        return data
