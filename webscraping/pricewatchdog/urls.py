"""
URL configuration for webscraping project.

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

# urls.py
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib import admin
from .views import scrape_amazon
from .views import track_price
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', views.index, name='index'),

    path('signup/',views.Signup,name='signup'),
    path('login/',views.Login,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),


    path('store/', views.store, name='store'),

    path('search/', views.search, name='search'),

    path('main/', views.main, name='main'),

    path("compare1/", views.compare1, name='compare1'),

    path('compare2/', views.compare2, name='compare2'),

    path("compare2/<int:id1>", views.compare2, name='compare2'),

    path("compare2/<int:id1>/<int:id2>", views.compare2, name='compare2'),

    # path('track-price/', views.track, name='track_price')
    path('track-price1/', views.track_price1, name='track_price1'),

    path('track-price/', views.track_price, name='track_price'),

    path('get_product_details/', views.get_product_details, name='get_product_details'),

    path('view/', views.view, name='view'),

    path('amazontutorial/' , scrape_amazon, name= 'scrape_amazon'),




]

# urlpatterns += staticfiles_urlpatterns()