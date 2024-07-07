from django.db import models
from category.models import Category
from account.models import User
# Create your models here.

class RentAdvertisment(models.Model):
  title=models.CharField(max_length=100)
  description=models.TextField()
  price=models.DecimalField(max_digits=10,decimal_places=2)
  category=models.ForeignKey(Category,related_name='advertisements',on_delete=models.CASCADE)
  owner=models.ForeignKey(User,related_name='advertisements',on_delete=models.CASCADE)
  is_approved=models.BooleanField(default=False)
  created_at=models.DateTimeField(auto_now_add=True)
  image=models.ImageField(upload_to='advertisement/images/')

  def __str__(self) -> str:
    return self.title