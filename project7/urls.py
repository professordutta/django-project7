"""project7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from test7 import views
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = 'Employee Management System'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add_record',views.add_record,name='add_record'),
    path('read_record',views.read_record,name='read_record'),
    path('search', views.search,name='search'),
    path('update_record',views.update_record,name='update_record'),
    path('update_info',views.update_info,name='update_info'),
    path('delete',views.delete,name='delete'),
    path('delete_info',views.delete_info,name='delete_info'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)