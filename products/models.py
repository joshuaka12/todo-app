from django.db import models
import uuid
from django.db.models import F
from django.db import transaction 
# Create your models here.

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100) 
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='categories')
    slug = models.SlugField(max_length=100, unique=True, help_text="A unique identifer for category")
    description = models.TextField()
    order = models.PositiveIntegerField(
        default=0, null=True, blank=True,
        help_text="The order in which the product should be displayed. lower number"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)
    is_active = models.BooleanField(default=True)
    in_sale = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100) 
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='products')
    slug = models.SlugField(max_length=100, unique=True, help_text="A unique identifer for products")
    Categories = models.ManyToManyField(Category, related_name = 'products')
    description = models.TextField()
    order = models.PositiveIntegerField(
        default=0, null=True, blank=True,
        help_text="The order in which the product should be displayed. lower number"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)
    is_active = models.BooleanField(default=True)
    in_sale = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_place=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in order {self.order.id}"

class Order(models.Model):
     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='orders')
     products = models.ManyToManyField(Product, related_name = 'orders')
     is_active = models.ManyToManyField(default=True)
     created_at = models.DateTimeField(auto_now_add=True)
     upated_at = models.DateTimeField(auto_now=True)
     def _str_(self):
         return f"Order {self.id} by {self.user.username}"
      
@transaction.atomic
def create_order(user, cart_items):
    order = Order.objects.create(
        user=user,
        is_active=True
    )

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            unit_price=item.product.price
        )

    return order