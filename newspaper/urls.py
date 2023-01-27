from django.urls import path
from .views import (index,
                    NewspaperListView,
                    NewspaperDetailView,
                    TopicListView,
                    TopicDetailView,
                    RedactorListView,
                    RedactorDetailView,
                    TopicCreateView,
                    RedactorCreateView,
                    NewspaperUpdateView,
                    NewspaperDeleteView,
                    RedactorExperienceUpdateView,
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
    path("redactor/<int:pk>/", RedactorDetailView.as_view(),
         name="redactor-detail"),
    path("topic/create/", TopicCreateView.as_view(),
         name="topic-create"),
    path("redactor/create/", RedactorCreateView.as_view(),
         name="redactor-create"),
    path("newspaper/<int:pk>/update/", NewspaperUpdateView.as_view(),
         name="newspaper-update"),
    path("newspaper/<int:pk>/delete/", NewspaperDeleteView.as_view(),
         name="newspaper-delete"),
    path("redactor/<int:pk>/update", RedactorExperienceUpdateView.as_view(),
         name="redactor-update"),
]


app_name = "newspaper"
