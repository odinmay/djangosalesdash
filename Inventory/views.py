from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView
from .models import Product
from .forms import ProductForm


class ProductHome(ListView):
    model = Product


class CreateProduct(View):
    template_name = 'Inventory/product-create.html'

    def get(self, request):
        form = ProductForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = ProductForm(request.POST)
        ctx = {'form': form}

        if form.is_valid():
            new_prod = Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                cost=form.cleaned_data['cost'],
                sale_price=form.cleaned_data['sale_price'],
            )
            new_prod.save()
            return HttpResponseRedirect('/products')

        else:
            form = ProductForm()
        return render(request, self.template_name, ctx)


# class UpdateProduct(UpdateView):
#     def get(self):
#         pass
#
#     def post(self):
#         pass
#
#
class DetailProduct(DetailView):
    model = Product
    template_name = 'Inventory/product-detail.html'

    def get(self, request, pk):
        obj = Product.objects.get(id=pk)
        ctx = {'product': obj}
        return render(request, self.template_name, ctx)

# class DeleteProduct(View):
#     def get(self):
#         pass
#
#     def post(self):
#         pass
