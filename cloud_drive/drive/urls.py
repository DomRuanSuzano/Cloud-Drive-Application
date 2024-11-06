from django.urls import path
from .views import upload_file, register, user_login, user_logout, account_info, serve_user_file

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('register/', register, name='register'),
    path('', user_login, name='user_login'),  # URL para login
    path('logout/', user_logout, name='user_logout'),  # URL para logout
    path('account/', account_info, name='account_info'),
    path('file/<int:file_id>/', serve_user_file, name='serve_user_file'),

]
