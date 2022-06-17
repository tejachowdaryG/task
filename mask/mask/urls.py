"""mask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from account import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include("account.api.urls")),
    path('register/', views.registerPage),
    path('login/', views.loginPage),
    path('home/',views.home),
    path('TL/',views.Team_taskView),
    path('TM/',views.Team_modelView),
    path('Tform/',views.Team_taskFormView),
    path('Mform/',views.Team_modelFormView),
    path('Tdelete/<int:id>',views.Team_taskDelete),
    path('Tupdate/<int:id>',views.Team_taskUpdateView),
    path('Mdelete/<int:id>',views.Team_modelDelete),
    path('Mupdate/<int:id>',views.Team_modelUpdateView),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html")),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_resetsent.html")),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_resetconfirm.html")),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_resetcomplete.html"))

]
