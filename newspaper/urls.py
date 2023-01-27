from django.urls import path
from .views import (index,
                    NewspaperListView,
                    NewspaperDetailView,
                    TopicListView,
                    TopicDetailView,
                    )


urlpatterns = [
    path("", index, name="index"),
    path("newspaper/", NewspaperListView.as_view(),
         name="newspaper-list"),
    path("newspaper/<int:pk>/", NewspaperDetailView.as_view(),
         name="newspaper-detail"),
    path("topic/", TopicListView.as_view(),
         name="topic-list"),
    path("topic/<int:pk>/", TopicDetailView.as_view(),
         name="topic-detail"),
]


app_name = "newspaper"
