from django.urls import path

from . import views as views

urlpatterns = [
    path("", views.home),
    path("vazifalar/", views.vazifalar),
    path("kalendar/", views.kalendar, name="kalendar"),
    path("statistics/", views.statistics, name="statistics"),
    path("settings/", views.settings),
    path("view/", views.view),
    path("yangi_vazifa/", views.yangi_vazifa),
    path("vazifalarni qidirish/", views.vazifalarni_qidirish),
    path('', views.task_list_view, name='home_page'), 
    path('add-task/', views.task_list_view, name='add_task'),
    path('settings/', views.settings_view, name='settings'), 
    path('profile/', views.profile_view, name='profile_page'),
    path('settings/privacy/', views.privacy_settings, name='privacy_view'),
    path('', views.task_list, name='task_list'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('edit/task/<int:pk>/', views.edit_task, name='edit_task'),
]
