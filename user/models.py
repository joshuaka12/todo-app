from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=123)
    first_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username
    
class Score(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='score')
  value = models.IntegerField(default = 0)
        
  def __str__(self):
            return f"{self.user.username} - Score: {self.value}"