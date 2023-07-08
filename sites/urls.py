from django.urls import path
from .views import SiteList, SiteDetail, SiteImageList, SiteImageDetail, SiteActivityList, SiteActivityDetail, EateryList, EateryDetail, EateryImageList, EateryImageDetail, MenuItemList, MenuItemDetail

urlpatterns = [
    path('sites/images/<int:pk>/', SiteImageDetail.as_view(), name='site_image_detail'),
    path('sites/images', SiteImageList.as_view(), name='site_image_list'),
    path('sites/activities/<int:pk>/', SiteActivityDetail.as_view(), name='site_activity_detail'),
    path('sites/activities', SiteActivityList.as_view(), name='site_activity_list'),
    path('sites/<int:pk>/', SiteDetail.as_view(), name='site_detail'),
    path('sites/', SiteList.as_view(), name='site_list'),

    ##paths related to eateries
    path('eateries/menu/<int:pk>/', MenuItemDetail.as_view(), name='menu_item_detail'),
    path('eateries/menu', MenuItemList.as_view(), name='menu_item_list'),
    path('eateries/images/<int:pk>/', EateryImageDetail.as_view(), name='eatery_image_detail'),
    path('eateries/images', EateryImageList.as_view(), name='eatery_image_list'),
    path('eateries/<int:pk>/', EateryDetail.as_view(), name='eatery_detail'),
    path('eateries/', EateryList.as_view(), name='eatery_list'),
]
