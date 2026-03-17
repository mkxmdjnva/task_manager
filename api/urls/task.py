from django.urls import path

import api.views.task as views

urlpatterns = [
    path("tasks", views.TaskListView.as_view()),
    path("tasks/", views.TaskCreateView.as_view()),
    path("tasks/<int:pk>", views.TaskRetrieveView.as_view()),
    path("tasks/<int:pk>/", views.TaskUpdateView.as_view()),
    path("tasks/delete/<int:pk>/", views.TaskDeleteView.as_view()),
]