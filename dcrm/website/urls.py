from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),  # wenn in navbar.html auf "logout" referenziert wird, dann wird logout_user in views.py ausgeführt
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),  # localhost:8000/record/2
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
]
