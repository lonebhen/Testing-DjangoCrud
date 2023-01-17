from django.urls import path
from menus.models import Menu
from DjangoCrud import views

urlpatterns = [
    path('create/', views.create(Menu), name='create'),
    path('list/', views.list(Menu), name='list'),
    path('update/<str:pk>', views.update(Menu), name='update'),
    path('detail/<str:pk>', views.detail(Menu), name='detail'),
    path('delete/<str:pk>', views.delete(Menu), name='delete')

]