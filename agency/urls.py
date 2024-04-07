from django.urls import path

from agency.views import (
    index,
    TopicListView,
    RedactorListView,
    NewspaperViewList,
    RedactorCreateView,
    RedactorDetailView,
    NewspaperDetailView,
    NewspaperCreateView,
    NewspaperDeleteView,
    NewspaperUpdateView,
    TopicDetailView,
    RedactorDeleteView,
    RedactorUpdateView,
    TopicUpdateView,
    TopicDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("newspapers/", NewspaperViewList.as_view(), name="newspaper-list"),
    path("redactors/create", RedactorCreateView.as_view(), name="redactor-create"),
    path("newspapers/create/", NewspaperCreateView.as_view(), name="newspaper-create"),
    path("redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
    path(
        "newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"
    ),
    path(
        "newspapers/<int:pk>/delete/",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete",
    ),
    path(
        "newspapers/<int:pk>/update",
        NewspaperUpdateView.as_view(),
        name="newspaper-update",
    ),
    path("topics/<int:pk>/", TopicDetailView.as_view(), name="topic-detail"),
    path(
        "redactors/<int:pk>/delete",
        RedactorDeleteView.as_view(),
        name="redactor-delete",
    ),
    path(
        "redactors/<int:pk>/update",
        RedactorUpdateView.as_view(),
        name="redactor-update",
    ),
    path("topics/<int:pk>/update", TopicUpdateView.as_view(), name="topic-update"),
    path("topics/<int:pk>/delete", TopicDeleteView.as_view(), name="topic-delete"),
]

app_name = "agency"
