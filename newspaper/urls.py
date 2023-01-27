from django.urls import path
from .views import (index,
                    NewspaperListView,
                    NewspaperDetailView,
                    TopicListView,
                    TopicDetailView,
                    RedactorListView,
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
    path("redactor/", RedactorListView.as_view(),
         name="redactor-list"),
]


app_name = "newspaper"
