from django.urls import path
from .views import alienList, alienOne, boxList, boxOne

urlpatterns = [
    path('aliens/', alienList),
    path('boxes/', boxList),
    path('aliens/<int:pk>/', alienOne),
    path('boxes/<int:pk>/', boxOne),
]
