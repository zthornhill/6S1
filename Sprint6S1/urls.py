from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from subPortfolio import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),
    path('', views.user_list),
    url(r'^api/users/$', views.user_list),
    url(r'^api/users/(?P<pk>[0-9]+)$', views.getUser),
    path('subscriptions/', views.subscription_list),
    url(r'^api/subscriptions/$', views.subscription_list),
    url(r'^api/subscriptions/(?P<pk>[0-9]+)$', views.getSubscription),
]

