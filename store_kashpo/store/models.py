from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# class Color(models.Model):
#     ANY = 1
#     WHITE = 2
#     INDIAN_TREE = 3
#     WENGE = 4
#
#     COLOR = (
#         (WHITE, 'Белый'),
#         (INDIAN_TREE, 'Индийское дерево'),
#         (WENGE, 'Венге'),
#         (ANY, 'Любой')
#     )
#
#     color = models.IntegerField(choices=COLOR, default=ANY)
#
#     def __str__(self):
#         return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, default=None)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.CharField(max_length=200,null=True, blank=True)
    is_active = models.BooleanField(default=False)
    # image = models.ImageField(null=True, blank=True)
    # color = models.ForeignKey(Color, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=100, null=True,blank=True, default='Любой')


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

