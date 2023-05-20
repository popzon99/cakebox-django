"""cakebox URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings


from cake.views import create_cake, home_cakes, view_cake, update_cake, delete_cake,About,send_gmail,all_cakes,user_signup,user_login,user_logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',create_cake, name='create_cake'),
    path('', home_cakes, name='list_cakes'),
    path('all/', all_cakes, name='all_cakes'),
    path('about/',About, name='about'),
    path('contact/',send_gmail,name='contact'),
    path('<int:pk>/', view_cake, name='view_cake'),
    path('<int:pk>/update/', update_cake, name='update_cake'),
    path('<int:pk>/delete/', delete_cake, name='delete_cake'),
    path('signup/', user_signup,name='signup'),
    path('login/', user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    #path('<int:pk>/', cake_detail, name='cake_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
