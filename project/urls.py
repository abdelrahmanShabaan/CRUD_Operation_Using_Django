"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from student.views import signup ,login , signout  ,students ,create_student , delete_student ,edit_student ,contact  ,Student_create_form




urlpatterns = [
    path('admin/', admin.site.urls),
     path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('signout/', signout, name='signout'),
    path('students/', students, name='students'),
    path('create_student/', create_student, name='create_student'),
    path('edit_student/<int:id>', edit_student, name='edit_student'),
    path('delete_student/<int:id>', delete_student, name='delete_student'),
    path('contact/', contact, name='contact'),
    path('Student_create_form/', Student_create_form, name='Student_create_form'),

]
