"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views

urlpatterns = [
    path('producer/', views.ProducerList.as_view(), name="producer-list"),
    path('producer/<int:pk>', views.ProducerDetail.as_view(), name="producer-detail"),
    path('farm/', views.FarmList.as_view(), name="farm"),
    path('farm-list/<int:pk_producer>', views.FarmList.as_view(), name="farm-list"),
    path('farm/<int:pk>', views.FarmDetail.as_view(), name="farm-detail"),
    path('area/', views.AreaList.as_view(), name="area"),
    path('area-list/<int:pk_farm>', views.AreaList.as_view(), name="area-list"),
    path('area/<int:pk>', views.AreaDetail.as_view(), name="area-detail"),
    path('dashboard/total-farm/', views.DashboardData.as_view({'get': 'get_total_farm'}),
         name="get_total_farm"),
    path('dashboard/total-area/', views.DashboardData.as_view({'get': 'get_total_area'}),
         name="get_total_area"),
    path('dashboard/total-state/', views.DashboardData.as_view({'get': 'get_total_by_state'}),
         name="get_total_state"),
    path('dashboard/total-crop/', views.DashboardData.as_view({'get': 'get_total_by_crop'}),
         name="get_total_crop"),
    path('dashboard/total-type/', views.DashboardData.as_view({'get': 'get_total_by_type'}),
         name="get_total_type"),
]
