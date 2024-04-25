from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,View,DetailView
from .models import Customers,Account,Card
from django.shortcuts import redirect



class IndexViews(ListView):
    template_name = "index.html"
    model = Customers

class AddCustomerView(ListView):
    template_name = "add_customers.html"
    model = Customers

class CustomerDetailView(DetailView):
    model = Customers
    template_name = 'customers_detail.html'
    context_object_name = 'customer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.get_object()
        context['accounts'] =Account.objects.filter(customer=customer)
        return context

class AccountCardsListView(ListView):
    model = Card
    template_name = 'account_cards.html'
    context_object_name = 'cards'

    def get_queryset(self):
        account_id = self.kwargs['pk']
        account = get_object_or_404(Account, pk=account_id)
        return Card.objects.filter(account=account)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account_id = self.kwargs['pk']
        context['account'] = get_object_or_404(Account, pk=account_id)
        return context


# Create your views here.
