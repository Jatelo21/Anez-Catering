from django.urls import path
from catering.views import ProductCreateView,ProductListView,ProductDetailView,ProductDeleteView,ProductUpdateView,HomePageView
app_name="catering"
urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('product/add/', ProductCreateView.as_view(template_name="product_create.html"), name='product_add'),
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/detail/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]