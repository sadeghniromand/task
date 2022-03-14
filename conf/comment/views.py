from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from . import forms
from product.models import Product


# Create your views here.


class CreateCommentView(LoginRequiredMixin, CreateView):
    form_class = forms.CreatCommentForm
    template_name = 'comment/create.html'

    def form_valid(self, form):
        a = 1
        form = form.save(commit=False)
        form.username = self.request.user.username
        form.email = self.request.user.email
        form.product = get_object_or_404(Product, pk=int(self.kwargs['pk']))
        b = 1
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('product:detail_product', kwargs={'pk': self.kwargs['pk']})
