from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.core.mail import send_mail
from django.db import models


# Create your models here.

class Admin(models.Model):
    pass


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/')
    price = models.FloatField()
    text = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    country = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    adress1 = models.CharField(max_length=50)
    adress2 = models.CharField(max_length=50)
    Town = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Post = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
