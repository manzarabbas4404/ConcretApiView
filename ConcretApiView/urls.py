
from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('StudentApi/',views.List_Create_Api.as_view(), name='api1'),
    path('StudentApi/<int:pk>/', views.Retrieve_Update_Destroy.as_view(), name='api2')
]
