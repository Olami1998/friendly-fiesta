from django.urls import path
from .views import home, about, contact


urlpatterns = [ 
    path('', home), #a
    path('about-me/', about), #b
    path('contact-me/', contact) #c
]
  



#www.leki.com/  home view
#www.leki.com/about about view