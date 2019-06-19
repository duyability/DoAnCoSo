from django.urls import path
from search.views import search, search_onsite

app_name='search'
urlpatterns = [
    path('timkiem_job', search, name='search'),
    path('timkiem_onsite', search_onsite, name='search_onsite'),
]