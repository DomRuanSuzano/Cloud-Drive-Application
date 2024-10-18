from django.urls import path
from .views import upload_file, register, user_login, user_logout

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),  # URL para login
    path('logout/', user_logout, name='user_logout'),  # URL para logout
]
