from django.urls import re_pathfrom .views import (                        StatusListSearchAPIView,                    PizzaCreateAPIView,                    PizzaDetailAPIView,                    PizzaUpdateAPIView,                    PizzaDeleteAPIView,                )urlpatterns=[    re_path(r'^$',StatusListSearchAPIView.as_view()),    re_path(r'^create/$',PizzaCreateAPIView.as_view()),    re_path(r'^(?P<pk>\d+)/$',PizzaDetailAPIView.as_view()),    re_path(r'^(?P<pk>\d+)/update/$',PizzaUpdateAPIView.as_view()),    re_path(r'^(?P<pk>\d+)/delete/$',PizzaDeleteAPIView.as_view()),]