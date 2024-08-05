from django.urls import path
from . import views


urlpatterns = [
    
    path('signup',views.signup,name='signup_api'),
    path('login', views.login, name='login_api'),
    path('add_medicine', views.add_medicine, name='addmedicineapi'),
    path('list_medicine', views.list_medicines, name='listmedicineapi'),
    path('<int:pk>/edit_data', views.edit_data, name='editdataapi'),
    path('<int:pk>/delete_data', views.delete_data, name='deletedataapi')
]
