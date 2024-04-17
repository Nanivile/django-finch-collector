from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    path('finchs/', views.finchs_index, name='index'),
    path('finchs/<int:finch_id>', views.finchs_detail, name='detail'),
    path('finchs/create', views.FinchCreate.as_view(), name='finchs_create'),
    path('finchs/<int:pk>/update', views.FinchUpdate.as_view(), name='finchs_update'),
    path('finchs/<int:pk>/delete', views.FinchDelete.as_view(), name='finchs_delete'),
    path('finchs/<int:finch_id>/add_grabbeditem/', views.add_grabbeditem, name='add_grabbeditem'),
    path('finchs/<int:finch_id>/assoc_favoritefood/<int:favoritefood_id>', views.assoc_favoritefood, name='assoc_favoritefood'),
    path('finchs/<int:finch_id>/rm_assoc_favoritefood/<int:favoritefood_id>', views.rm_assoc_favoritefood, name='rm_assoc_favoritefood'),
    path('favoritefood/', views.fav_foods_index, name='favoritefood_index'),
    path('favoritefood/<int:pk>', views.FoodDetail.as_view(), name='favoritefood_detail'),
    path('favoritefood/create/', views.FoodCreate.as_view(), name='favoritefood_create'),
    path('favoritefood/<int:pk>/update/', views.FoodUpdate.as_view(), name='favoritefood_update'),
    path('favoritefood/<int:pk>/delete/', views.FoodDelete.as_view(), name='favoritefood_delete'),
]