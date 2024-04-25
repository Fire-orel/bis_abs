from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,View,DetailView,UpdateView,DeleteView
from .models import Customers,Account,Card
from django.shortcuts import redirect
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy



class IndexViews(ListView):
    template_name = "index.html"
    model = Customers



class AddCustomerView(ListView):
    template_name = "add_customers.html"
    model = Customers

    def post(self, request, **kwargs):
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        passport_number = request.POST.get('passport_number')
        password_issue_data = request.POST.get('password_issue_data')

        check_passport_number=Customers.get_customer_by_paspord(passport_number)

        if not check_passport_number:
            customer=Customers(last_name = last_name,
                               first_name = first_name,
                               middle_name = middle_name,
                               gender = gender,
                               address = address,
                               email=email,
                               phone_numder = phone,
                               password_number = passport_number,
                               password_issue_data = password_issue_data,
                               date_of_birth=date_of_birth)
            customer.save()
            # request.session["customer"]=email


            response=HttpResponseRedirect(redirect_to="/")
            return response
        else:
            response=HttpResponseRedirect(redirect_to=".")
            return response


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
    def 

class EditCustomerView(UpdateView):
    model = Customers
    fields = []  # Список полей, которые будут доступны для редактирования
    template_name = 'edit_customer.html'
    success_url = '/customer_list/'  # URL для перенаправления после успешного редактирования

    def get_object(self, queryset=None):
        # Получаем клиента по его идентификатору
        return get_object_or_404(Customers, id=self.kwargs['pk'])

    def post(self, request, **kwargs):
        customer = get_object_or_404(Customers, id=self.kwargs['pk'])
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        password_number = request.POST.get('passport_number')
        password_issue_data = request.POST.get('password_issue_data')

        # check_passport_number=Customers.get_customer_by_paspord(password_number)

        customer.last_name = last_name
        customer.first_name = first_name
        customer.middle_name = middle_name
        customer.gender = gender
        customer.address = address
        customer.email = email
        customer.phone_numder = phone
        customer.password_number = password_number
        customer.password_issue_data = password_issue_data
        customer.date_of_birth = date_of_birth



        customer.save()
        # request.session["customer"]=email


        response=HttpResponseRedirect(redirect_to = '/')
        return response
class CustomerDeleteView(DeleteView):
    model = Customers
    template_name = 'confirm_delete_customer.html'
    success_url = reverse_lazy('customer_list')
# Create your views here.
