from django.urls import path

from user_profile.views import user_profile, register_page, log_out, login_page

urlpatterns = [
    path('', user_profile, name='profile'),
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('log_out/', log_out, name='log_out')
]
