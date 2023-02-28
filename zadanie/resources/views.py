from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Resources
from .serializers import ResourcesSerializer


class ResourcesViewSet(mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer

    def list(self, request):
        queryset = self.get_queryset()
        return Response(
            {
                'resources': ResourcesSerializer(queryset, many=True).data,
                'total_count': Resources.objects.count()
            })


@api_view(['GET'])
def TotalCost(request):
    queryset = Resources.objects.all()
    total_cost = 0
    for resource in queryset:
        total_cost += resource.amount * resource.price
    return Response({"total_cost": total_cost})
