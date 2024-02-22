from django.contrib import admin

from .models import Category, Product, Feedback
from accounts.models import User
from orders.models import Order

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Feedback)
admin.site.register(User)
admin.site.register(Order)
