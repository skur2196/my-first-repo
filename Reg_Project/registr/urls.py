from django.urls import path
from registr.views import index, choose, register_list, adding, logout, details


urlpatterns = [
    path('', index),
    path('register/', choose),
    path('register/<int:patient_type>/', register_list),
    path('register/<int:patient_type>/add', adding),
    path('logout/', logout),
    path('register/<int:patient_type>/<int:patient_pk>/', details),
]
