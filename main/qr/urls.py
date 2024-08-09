from django.urls import path
from .views import register,retrieve,search,home,update_qr_code,delete_qr_code,get_data

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('retrieve/<int:pk>/', retrieve, name='retrieve'),
    path('search/', search, name='search'),
    path('qr-code/update/<int:id>/', update_qr_code, name='update_qr_code'),
    path('qr-code/delete/<int:id>/', delete_qr_code, name='delete_qr_code'),
    path('qr-codes/', get_data, name='get-data'),

]
