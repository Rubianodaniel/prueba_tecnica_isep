from django.urls import path
from crud_app.views import ValidateListCreateView, ValidateUpdateOrDelete

urlpatterns = [
    path('api/data/', ValidateListCreateView.as_view(), name='data-list-create'),
    path('api/data/<int:pk>/', ValidateUpdateOrDelete.as_view(), name='data-update-destroy'),
]
