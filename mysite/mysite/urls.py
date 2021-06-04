"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from form import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('create-form/', views.index, name="index"),
    path('forms/', views.FormListView.as_view(), name="forms"),
    path('form/<int:pk>', views.FormDetailView.as_view(), name="form"),
    path('update-form/<int:pk>', views.FormUpdate.as_view(), name="update-form"),
    path('form/<int:pk>/delete/', views.FormDelete.as_view(), name="form-delete"),
    path('forms/', views.FormListView.as_view(), name="forms"),
    path('queries/', views.UserQueryList.as_view(), name="queries"),
    path('query/<int:pk>', views.UserQueryDetailView.as_view(), name="query"),

]
