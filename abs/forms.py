# from django import forms
# from .models import Customers

# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customers
#         fields = ['first_name', 'last_name', 'email', 'phone']  # Поля, которые будут отображаться в форме

#     # def __init__(self, *args, **kwargs):
#     #     super(CustomerForm, self).__init__(*args, **kwargs)
#     #     self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'First Name'})
#     #     self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Last Name'})
#     #     self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
#     #     self.fields['phone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Phone'})
