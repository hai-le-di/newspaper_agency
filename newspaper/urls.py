from django.urls import path
from django.contrib.auth.views import LogoutView
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
                    RedactorUpdateView,
                    RedactorDeleteView,
                    NewspaperCreateView,
                    login_view,
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
    path("newspaper/create/", NewspaperCreateView.as_view(),
         name="newspaper-create"),
    path("newspaper/<int:pk>/delete/", NewspaperDeleteView.as_view(),
         name="newspaper-delete"),
    path("redactor/<int:pk>/update", RedactorUpdateView.as_view(),
         name="redactor-update"),
    path("redactor/<int:pk>/delete/", RedactorDeleteView.as_view(),
         name="redactor-delete"),
    path("login/", login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout")
]


app_name = "newspaper"
