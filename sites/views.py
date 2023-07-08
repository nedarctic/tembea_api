from rest_framework import generics
from .models import Site, SiteActivity, SiteImage, Eatery, EateryImage, MenuItem
from .serializers import SiteSerializer, SiteActivitySerializer, SiteImageSerializer, EaterySerializer, EateryImageSerializer, MenuItemSerializer

class SiteList(generics.ListCreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class SiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class SiteActivityList(generics.ListCreateAPIView):
    queryset = SiteActivity.objects.all()
    serializer_class = SiteActivitySerializer

class SiteActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SiteActivity.objects.all()
    serializer_class = SiteActivitySerializer

class SiteImageList(generics.ListCreateAPIView):
    queryset = SiteImage.objects.all()
    serializer_class = SiteImageSerializer

class SiteImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SiteImage.objects.all()
    serializer_class = SiteImageSerializer

class EateryList(generics.ListCreateAPIView):
    queryset = Eatery.objects.all()
    serializer_class = EaterySerializer

class EateryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Eatery.objects.all()
    serializer_class = EaterySerializer

class EateryImageList(generics.ListCreateAPIView):
    queryset = EateryImage.objects.all()
    serializer_class = EateryImageSerializer

class EateryImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EateryImage.objects.all()
    serializer_class = EateryImageSerializer

class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
