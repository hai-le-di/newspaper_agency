from django.shortcuts import render
from django.views import generic

from newspaper.models import (Redactor,
                              Newspaper,
                              Topic)


def index(request):
    """View function for the home page of the site."""

    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_topics = Topic.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
        "num_topics": num_topics,
        "num_visits": num_visits + 1,
    }

    return render(request, "newspaper/index.html", context=context)


class NewspaperListView(generic.ListView):
    model = Newspaper
    paginate_by = 10


class NewspaperDetailView(generic.DetailView):
    model = Newspaper
    paginate_by = 5


class TopicListView(generic.ListView):
    model = Topic
    paginate_by = 5


class TopicDetailView(generic.DetailView):
    model = Topic
    paginate_by = 5
