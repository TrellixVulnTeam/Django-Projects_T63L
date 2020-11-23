from django.contrib import adminfrom django.urls import path,re_pathfrom .views import (                            ProductListView,                            # product_list_view,                            # ProductDetailView,                            # product_detail_view,                            # ProductFeaturedListView,                            # ProductFeaturedDetailView,                            ProductDetailSlugView,                            ProductDownloadView,                        # category_wise                            )app_name='products'urlpatterns = [    re_path(r'^$', ProductListView.as_view(),name='list'),    re_path(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(),name='detail'),    re_path(r'^(?P<slug>[\w-]+)/(?P<pk>\d+)/$', ProductDownloadView.as_view(),name='download'),    # re_path(r'^get_category_wise_product/$', category_wise,name='product_category_wise'),    # re_path(r'^featured/$', ProductFeaturedListView.as_view(),),    # re_path(r'^products-fbv/$', product_list_view,),    # re_path(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view(),),    # re_path(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view(),),    # re_path(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view,),]