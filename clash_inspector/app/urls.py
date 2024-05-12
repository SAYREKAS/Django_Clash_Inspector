from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from user_profile.views import register_page, login_page, log_out

urlpatterns = [
    path('admin/', admin.site.urls, ),
    path('', include('search.urls')),
    path('profile/', include('user_profile.urls')),
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('log_out/', log_out, name='log_out')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
