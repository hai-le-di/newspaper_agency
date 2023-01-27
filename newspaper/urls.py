from django.urls import path
from .views import (index,
                    NewspaperListView,
                    )


urlpatterns = [
    path("", index, name="index"),
    path("newspaper/", NewspaperListView.as_view(),
         name="newspaper-list"),
]


app_name = "newspaper"
