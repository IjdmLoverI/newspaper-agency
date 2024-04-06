from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from agency.models import Redactor, Topic, Newspaper


@login_required
def index(request):
    """View function for the home page of the site."""
    num_redactors = Redactor.objects.all().count()
    num_topics = Topic.objects.all().count()
    num_newspapers = Newspaper.objects.all().count()

    context = {
        "num_redactors": num_redactors,
        "num_topics": num_topics,
        "num_newspapers": num_newspapers,
    }
    return render(request, "agency/index.html", context=context)
