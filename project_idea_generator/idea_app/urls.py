from django.urls import path
from . import views

app_name = 'idea_app'

urlpatterns = [
    # Example:
    path('', views.home_view, name='home'),
]
