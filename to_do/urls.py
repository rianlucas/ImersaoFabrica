from django.urls import path
from .views import home, update, delete

urlpatterns = [
    path('', home,  name = 'home'),
    path('create/', home, name = 'create'),
    path('update/<int:pk>/', update, name = 'update'),
    path('delete/<int:pk>/', delete, name = 'delete'),

]
