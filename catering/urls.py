
from django.urls import path
from catering.views import ProductCreateView,ProductListView,ProductDetailView,ProductDeleteView,ProductUpdateView,HomePageView,ContactPageView,AboutPageView,ReservationPageView,register_request,login_request,logout_request
app_name="catering"
urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about',AboutPageView.as_view(),name='about'),
    path('contact',ContactPageView.as_view(),name='contact'),
    path('reserve', ReservationPageView.as_view(),name='reserve'),
    path('register', register_request,name='register'),
    path('login',login_request,name='login'),
    path('logout',logout_request,name="logout"),
    path('product/add/', ProductCreateView.as_view(template_name="product_create.html"), name='product_add'),
    path('menu/', ProductListView.as_view(), name='menu'),
    path('product/<int:pk>/detail/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
