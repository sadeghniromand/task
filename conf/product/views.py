from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.urls import reverse
from . import models, forms


class Home(TemplateView):
    template_name = 'base/home.html'


class CreateProductView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = forms.CreateProductForm
    permission_required = 'product.add_product'
    template_name = 'product/create.html'

    def get_success_url(self):
        return reverse('home')


class ListProductView(ListView):
    model = models.Product
    template_name = 'product/list.html'

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(is_active=True)
        return query


class DetailProductView(DetailView):
    queryset = models.Product.objects.filter(is_active=True)
    template_name = 'product/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = self.object.comment()
        return context
