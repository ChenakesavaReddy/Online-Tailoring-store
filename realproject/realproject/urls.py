"""
URL configuration for realproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from tkinter.font import names

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from realapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('view_contact',views.view_contact,name='view_contact'),
    path('about', views.about, name='about'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('admin_index', views.admin_index, name='admin_index'),
    path('add_notification',views.add_notification,name='add_notification'),
    path('view_notification',views.view_notification,name='view_notification'),
    path('admin_change_password',views.admin_change_password,name='admin_change_password'),
    path("delete_notification/<int:id>/", views.delete_notification, name="delete_notification"),
    path("admin_view_customer",views.admin_view_customer,name='admin_view_customer'),
    path("admin_view_designer",views.admin_view_designer,name='admin_view_designer'),
    path('accept_customer/<int:id>/',views.accept_customer,name='accept_customer'),
    path('decline_customer/<int:id>/',views.decline_customer,name='decline_customer'),
    path('accept_designer/<int:id>/', views.accept_designer, name='accept_designer'),
    path('decline_designer/<int:id>/', views.decline_designer, name='decline_designer'),

    path('customer_login',views.customer_login,name='customer_login'),
    path('validate_otp', views.validate_otp, name='validate_otp'),
    path("customer_registration/", views.customer_registration, name="customer_registration"),
    path('customer_index',views.customer_index,name='customer_index'),
    path('customer_view_notification',views.customer_view_notification,name='customer_view_notification'),
    path('customer_change_password',views.customer_change_password,name='customer_change_password'),
    path('customer_forgot_password',views.customer_forgot_password,name='customer_forgot_password'),
    path('validate_forgot_otp',views.validate_forgot_otp,name='validate_forgot_otp'),
    path('initiate_forgot_password',views.initiate_forgot_password,name='initiate_forgot_password'),
    path('profile',views.profile,name='profile'),
    path('customer_profile_update/<int:id>/',views.customer_profile_update,name='customer_profile_update'),
    path('delete_profile/<int:id>/', views.delete_profile, name='delete_profile'),
    path('customer_logout',views.customer_logout,name='customer_logout'),
    path('customer_view_designer',views.customer_view_designer,name='customer_view_designer'),
    path('customer_view_designer_detail/<int:id>/', views.customer_view_designer_detail, name='customer_view_designer_detail'),
    path("customer/designer/<int:id>/services/", views.customer_view_designer_services,name="customer_view_designer_services"),
    path("book_service/<int:service_id>/", views.book_service, name="book_service"),
    path('view_orders/', views.view_orders, name='view_orders'),
    path('add_review/<int:booking_id>/', views.add_review, name='add_review'),
    path('customer_view_reviews/<int:designer_id>/', views.customer_view_reviews, name='customer_view_reviews'),


    path('designer_login',views.designer_login,name='designer_login'),
    path('validate_designer_otp',views.validate_designer_otp,name='validate_designer_otp'),
    path('designer/forgot-password/', views.initiate_designer_forgot_password, name='initiate_designer_forgot_password'),
    path('designer/validate-forgot-otp/', views.validate_designer_forgot_otp, name='validate_designer_forgot_otp'),
    path('designer/reset-password/', views.designer_forgot_password, name='designer_forgot_password'),
    path('designer_registration',views.designer_registration,name='designer_registration'),
    path('designer_index',views.designer_index,name='designer_index'),
    path('designer_profile/', views.designer_profile, name='designer_profile'),
    path("designer_change_password",views.designer_change_password,name="designer_change_password"),
    path("designer_update_profile/<int:id>/", views.designer_update_profile, name="designer_update_profile"),
    path("delete_designer_profile/<int:id>/",views.delete_designer_profile,name='delete_designer_profile'),
    path('designer_gallery_upload/', views.designer_gallery_upload, name='designer_gallery_upload'),
    path('delete_image/<int:image_id>/', views.delete_image, name='delete_image'),
    path('designer_add_service/', views.designer_add_service, name='designer_add_service'),
    path('designer_view_services/<int:designer_id>/',views.designer_view_services,name="designer_view_services"),
    path('designer_edit_service/<int:service_id>/', views.designer_edit_service, name="designer_edit_service"),
    path('designer_delete_service/<int:service_id>/', views.designer_delete_service, name='designer_delete_service'),
    path("designer/<int:designer_id>/orders/", views.designer_order, name="designer_order"),
    path('designer/<int:designer_id>/reviews/', views.designer_view_reviews, name='designer_view_reviews'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)