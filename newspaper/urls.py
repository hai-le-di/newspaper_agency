from django.urls import path
from .views import (index,
                    NewspaperListView,
                    NewspaperDetailView,
                    )


urlpatterns = [
    path("", index, name="index"),
    path("newspaper/", NewspaperListView.as_view(),
         name="newspaper-list"),
    path("newspaper/<int:pk>/", NewspaperDetailView.as_view(),
         name="newspaper-detail"),
]


app_name = "newspaper"
