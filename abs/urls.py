from django.urls import path

from abs.views import IndexViews,AddCustomerView,CustomerDetailView,AccountCardsListView

urlpatterns = [
    path('', IndexViews.as_view(), name = "customer_list"),
    path('add_customer/', AddCustomerView.as_view(),name='add_customer'),
    path('customer_detail/<int:pk>', CustomerDetailView.as_view(),name='customer_detail'),
    path('acount_cards/<int:pk>', AccountCardsListView.as_view(),name='account_cards'),

]
