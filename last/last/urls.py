from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('employee/', include('employee.urls')),
    path('dashboard/', include('dashboard.urls')),
]