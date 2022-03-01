from django.contrib import admin
from django.urls import path
from Quiz.views import *
from django.conf import settings

urlpatterns = [
    path('login/', loginPage,name='login'),
    path('admin/', admin.site.urls),
    path('', home,name='home'),
   # path('addQuestion/', addQuestion,name='addQuestion'),
    path('logout/', logoutPage,name='logout'),
    path('register/', registerPage,name='register'),

]