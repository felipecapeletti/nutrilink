from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ItemSerializer
from .models import Item



@api_view(["GET"])
def health(request):
    return Response({"status": "ok", "service": "backend", "version": "1.0"})

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by("-id")
    serializer_class = ItemSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    return Response({"username": user.username, "email": user.email})