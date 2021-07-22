from django.urls import path#This import allows us to use the path function(within urlpatterns)
from . import views #This will import our view.py module from the main project directory


"""
Please note the it must be 'urlpatterns' and not 'urlpattern'. This will be name specific and will cause an error otherwise
path() will allow us to create a url for a specified view

Note that more documention on views can be found in the main project directory 'tutorial_1'
"""
urlpatterns = [
    path('', views.index, name='index')

]