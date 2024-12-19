
from django.urls import path
from . import views

#Defining the URL patterns for this Django app
urlpatterns = [
#Route for the root URL ("") which maps to the `home` view
#`name="home"` provides a unique name for this URL pattern for later reference
    path("", views.home, name="home")
]