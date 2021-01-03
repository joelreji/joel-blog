from django.urls import path
from . import views

urlpatterns = [
    path("portfolio/", views.portfolio_index, name="portfolio_index"),
    path("portfolio/<int:id>/", views.portfolio_detail, name="portfolio_detail"),
]
