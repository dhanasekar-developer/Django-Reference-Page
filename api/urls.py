from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('',views.employee_view, name="employee_view"),
    path('data/', views.response_view, name="response_view"),
]
