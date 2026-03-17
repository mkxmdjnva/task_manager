from django.urls import path, include

urlpatterns = [
    path("", include("api.urls.task")),
    path("", include("api.urls.category")),
]