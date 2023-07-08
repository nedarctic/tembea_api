from rest_framework import serializers
from .models import Site, SiteActivity, SiteImage, Eatery, EateryImage, MenuItem

##Serializers related to sites
class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('region', 'county', 'name', 'description', 'opening_hour', 'closing_hour', 'availability_during_week', 'number_of_times_visited', 'latitude', 'longitude',)
        model = Site

class SiteImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('site', 'name', 'image',)
        model = SiteImage

class SiteActivitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'charges', 'site',)
        model = SiteActivity

##Serializers related to eateries
class EaterySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('site', 'name', 'description', 'opening_hour', 'closing_hour', 'latitude', 'longitude',)
        model = Eatery

class EateryImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('eatery', 'name', 'image_url',)
        model = EateryImage

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('eatery', 'category', 'meal_name', 'charges',)
        model = MenuItem
