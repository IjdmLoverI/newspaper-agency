from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from agency.models import Redactor, Newspaper, Topic


class RedactorCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "email",
            "first_name",
            "last_name",
            "years_of_experience",
        )


class NewspaperCreateForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=Redactor.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    topic_name = forms.CharField(max_length=255)

    class Meta:
        model = Newspaper
        fields = ["title", "content", "publishers", "topic_name"]

    def save(self, commit=True):
        newspaper = super().save(commit=False)
        topic_name = self.cleaned_data.get("topic_name")
        topic, created = Topic.objects.get_or_create(name=topic_name)
        newspaper.topic = topic
        if commit:
            newspaper.save()
            self.save_m2m()
        return newspaper


class TopicCreateForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["name"]


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search"}),
    )
