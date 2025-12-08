from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('quize/<int:category_id>/', quiz_home, name = "quize"),
    path('signup/', sign_up_view, name="signup"),
    path('login/', sign_in_view, name="signin"),
    path('logout/', logout_view, name = "logout"),
    path('my-score/', my_score, name="scores")
]