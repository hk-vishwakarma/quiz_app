from django.urls import path
from .views import *

urlpatterns = [
    path('', quiz_home, name = "home"),
    path('register/', sign_up_view, name="register"),
    path('sign-in/', sign_in_view, name="signin"),
    path('logout/', logout_view, name = "logout"),
]