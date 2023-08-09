from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login_view_name'),
    path('logout/', views.user_logout, name='logout_view_name'),
    # other urls...
]
