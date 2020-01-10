from django.urls import path

from . import views

app_name = 'wojtekmeble'

urlpatterns = [
    path('', views.index, name='index'),
    path('RecentRealizations', views.RecentRealizations,
         name='RecentRealizations'),
]
