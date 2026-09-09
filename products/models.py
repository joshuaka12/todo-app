from django.db import models
import uuid
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
    
    
class products(models.Model):
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
    
    