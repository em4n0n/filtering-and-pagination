from rest_framework.response import Response
from rest_framework import viewsets
from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your views here.

class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer