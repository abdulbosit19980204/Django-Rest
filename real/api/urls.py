from django.urls import path
from .views import TodoViewSet

urlpatterns = [
    path('', TodoViewSet.as_view({"get": "list"})),
    path('<int:pk>/', TodoViewSet.as_view({"get": "retrieve"})),
]
