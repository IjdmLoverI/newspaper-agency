from django.urls import path

from agency.views import (
    index,
    TopicListView,
    RedactorListView,
    NewspaperViewList
)

urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("newspaper/", NewspaperViewList.as_view(), name="newspaper-list")
]

app_name = "agency"
