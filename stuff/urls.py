from django.urls import path
from .views import StuffList, StuffDetail

urlpatterns = [
    path("", StuffList.as_view(), name="stuff_list"),
    path("<int:pk>/", StuffDetail.as_view(), name="stuff_detail"),
]