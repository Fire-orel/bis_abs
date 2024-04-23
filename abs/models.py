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
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = "Дата открытие счёта")

    def __str__(self):
        return f"{self.pk} {self.last_name} {self.first_name} {self.middle_name}"

class Currencys (models.Model):
    name = models.CharField(max_length = 150, verbose_name = "Валюта", unique = True)
    code = models.CharField(max_length = 3, unique = True)
    symbol = models.CharField(max_length = 5, blank = True, null = True)

class Account (models.Model):

    customer = models.ForeignKey(Customers, on_delete = models.CASCADE)
    account_type = models.CharField(max_length = 1, choices = [("Д", "Дебетовый"), ("К","Кредитный"), ("Н","Накопительный")])
    currency = models.ForeignKey(Currencys, verbose_name = "Валюта",on_delete=models.CASCADE)
    status = models.CharField(max_length = 20, default = "active", verbose_name = "Статус счёта")


# Create your models here.
