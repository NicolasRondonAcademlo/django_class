from django.urls import path
from django.views.generic import TemplateView
from .views import CardListView, CardCreateView, CardUpdateView, BoxView
urlpatterns = [
    path("", CardListView.as_view(), name="card-list"),
    path("new", CardCreateView.as_view(), name="card-create"),
    path("edit/<int:pk>", CardUpdateView.as_view(), name="card-update"),
    path("box/<int:box_num>", BoxView.as_view(), name="box"),
]