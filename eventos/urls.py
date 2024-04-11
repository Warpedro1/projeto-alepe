from django.urls import path
from eventos.views import home_eventos, logout_view
#from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home_eventos', home_eventos, name='home_eventos'),
    #path('', logout_view)
    #path('logout/', LogoutView.as_view(), name='logout'),
]