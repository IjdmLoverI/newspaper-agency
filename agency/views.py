from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from agency.models import Redactor, Topic, Newspaper
from agency.forms import RedactorCreateForm, NewspaperCreateForm


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


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    paginate_by = 10


class TopicDetailView(LoginRequiredMixin, generic.DetailView):
    model = Topic
    success_url = reverse_lazy("agency:topic-detail")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 10


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreateForm
    success_url = reverse_lazy("agency:redactor-list")


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    success_url = reverse_lazy("agency:redactor-detail")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("agency:redactor-list")
    template_name = "agency/redactor_confirm_delete.html"


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    fields = ["username", "years_of_experience", "email"]

    def get_success_url(self):
        return reverse("agency:redactor-detail", kwargs={"pk": self.object.pk})


class NewspaperViewList(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    paginate_by = 10


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
    success_url = reverse_lazy("agency:newspaper-detail")


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperCreateForm
    success_url = reverse_lazy("agency:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("agency:newspaper-list")
    template_name = "agency/newspaper_confirm_delete.html"


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    fields = ["title", "content"]
    template_name = "agency/newspaper_form.html"

    def get_success_url(self):
        return reverse("agency:newspaper-detail", kwargs={"pk": self.object.pk})
