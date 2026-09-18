from django.urls import path
from Tracker import views

urlpatterns=[
    path('',views.user_login,name='user_login'),
    path('registartion',views.registration,name='registration'),
    path('home',views.home,name='home'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('add_job/',views.add_job,name='add_job'),
    path('delete_/<int:id>',views.delete_,name='delete_'),
    path('edit/<int:id>',views.edit,name='edit')
    
]