"""project_event_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("events-list/", views.EventsListView.as_view(), name="events-list"),
    path("edit/<int:event_id>/", views.EventDetailsView.as_view(), name="edit-event"),
    path("add/", views.AddEventView.as_view(), name="add-event"),
    path("search/", views.SearchEventView.as_view(), name="search-event"),
    path("fully-booked/", views.FullyBookedView.as_view(), name="fully-booked"),
]
