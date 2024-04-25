from django.db import models

class Customers (models.Model):
    last_name = models.CharField(max_length = 150, verbose_name = "Фамилия")
    first_name = models.CharField(max_length = 150,verbose_name = "Имя")
    middle_name = models.CharField(max_length = 150, verbose_name = "Отчество", blank = True)
    gender = models.CharField(max_length=1, choices=[("М", "Мужской"),("Ж", "Женский")])
    address = models.TextField(verbose_name = "Адрес проживание")
    email = models.EmailField(verbose_name = "Адрес электронной почты")
    phone_numder = models.CharField(max_length = 15,verbose_name = "Телефон")
    password_number = models.CharField(max_length = 10, verbose_name = "Номер паспорта")
    password_issue_data = models.DateField(verbose_name = "Дата получения паспорта")
    # created_at = models.DateTimeField(auto_now_add = True, verbose_name = "Дата открытие счёта")

    def __str__(self):
        return f"{self.pk} {self.last_name} {self.first_name} {self.middle_name}"

class Currencys (models.Model):
    name = models.CharField(max_length = 150, verbose_name = "Валюта", unique = True)
    code = models.CharField(max_length = 3, unique = True)
    symbol = models.CharField(max_length = 5, blank = True, null = True, default=' ')

    def __str__(self) :
        return f"{self.name}"

class Account (models.Model):

    customer = models.ForeignKey(Customers, on_delete = models.CASCADE,related_name = "customer")
    account_type = models.CharField(max_length = 1, choices = [("Д", "Дебетовый"), ("К","Кредитный"), ("Н","Накопительный")], default="Д")
    currency = models.ForeignKey(Currencys, verbose_name = "Валюта",on_delete=models.CASCADE, default='')
    status = models.CharField(max_length = 20, default = "active", verbose_name = "Статус счёта")
    opened_at = models.DateField(auto_now_add = True ,verbose_name = "Дата открытие счёта")
    closed_at = models.DateField(blank = True, null = True)

    def __str__(self):
        return f"{self.pk} {self.customer}"

class Card(models.Model):
    card_number = models.CharField(max_length = 16, unique = True, verbose_name = "Номер карты")
    expiration_date = models.DateField(verbose_name = "Срок окончание действие карты")
    customer = models.ForeignKey(Customers, on_delete = models.CASCADE)
    account = models.ForeignKey(Account, on_delete = models.CASCADE)



# Create your models here.
