from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    # path('signup/', views.signup, name='signup'),
    # path('forgot_password/', views.forgot_password, name='forgot_password'),
]
