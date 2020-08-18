from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    url(r'', include('blog.urls')),
]
