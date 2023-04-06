from django.urls import path

urlpatterns = [
    path('api/message/', RegisterAPI.as_view(), name='register'),
]