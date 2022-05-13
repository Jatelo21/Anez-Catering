from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView ,DeleteView ,UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from catering.models import Product
from django.urls import reverse,reverse_lazy
from .forms import AdminUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views h
class HomePageView(TemplateView):
    template_name='home.html'

class AboutPageView(TemplateView):
    template_name='about.html'

class ContactPageView(TemplateView):
    template_name='contact.html'


class ReservationPageView(TemplateView):
    template_name='reservation.html'

def register_request(request):
    if request.method == "POST":
        form = AdminUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "Registration successful")
            return redirect('catering:home')
        messages.error(request,"Unsuccessful registration.Invalid information")
    form = AdminUserForm()
    return render (request=request,template_name="register.html", context={"form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('catering:menu')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    form = AuthenticationForm()
    return render(request=request,template_name="login.html", context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out")
    return redirect('catering:home')


class ProductCreateView(CreateView, LoginRequiredMixin):
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



class ProductUpdateView(UpdateView,LoginRequiredMixin):
    model=Product
    fields=['category','price','name','quantity','date_manufacture','date_expiry_date','ingredients']
    template_name="product_update.html"
    success_url=reverse_lazy('catering:menu')



class ProductDeleteView(DeleteView, LoginRequiredMixin):
    model=Product
    template_name="product_delete.html"
    success_url=reverse_lazy('catering:menu')

