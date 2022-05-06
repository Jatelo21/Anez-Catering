from django.shortcuts import render
from django.views.generic.edit import CreateView ,DeleteView ,UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from catering.models import Product
from django.urls import reverse,reverse_lazy

# Create your views h
class HomePageView(TemplateView):
    template_name='home.html'

class ProductCreateView(CreateView):
    model = Product
    fields = ['category','price','name','quantity','date_manufacture','date_expiry_date','ingredients']
    template_name='product_create.html'
    success_url=reverse_lazy('catering:product_list')

class ProductListView(ListView):
    model=Product
    template_name='product_list.html'
    
class ProductDetailView(DetailView):
    model=Product
    context_object_name='products'
    template_name='product_detail.html'
    pk_url_kwarg = 'pk'
    

    def get_context_data(self,**kwargs):
        context=super(ProductDetailView, self).get_context_data(**kwargs)
        context['products']=Product.objects.all()
        return context

class ProductUpdateView(UpdateView):
    model=Product
    fields=['category','price','name','quantity','date_manufacture','date_expiry_date','ingredients']
    template_name="product_update.html"
    success_url=reverse_lazy('catering:product_list')

class ProductDeleteView(DeleteView):
    model=Product
    template_name="product_delete.html"
    success_url=reverse_lazy('catering:product_list')

