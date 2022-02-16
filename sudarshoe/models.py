from django.db import models
from django.core.exceptions import ValidationError
from accounts.models import Account

def validate_image(image):    
    file_size = image.size    
    limit_mb = 1
    if file_size > limit_mb * 1024 * 1024:  # 1kb = 1024b ; 1mb = 1024kb
        raise ValidationError("Max size of file is %s MB" % limit_mb)

class Product(models.Model):
    name=models.CharField(max_length=255, unique=True)
    image=models.ImageField(upload_to='sudarshoe/', validators=[validate_image], null=True)
    price=models.BigIntegerField()
    material=models.CharField(max_length=255)
    weight=models.IntegerField()
    size=models.CharField(max_length=255)
    stock=models.IntegerField()
    description=models.TextField()

    def __str__(self) -> str:
        return self.name
    
class Transaction(models.Model):
    customer=models.ForeignKey(Account, related_name='customer', on_delete=models.CASCADE, null=False)
    product=models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE, null=False)
    date=models.DateField(auto_now_add=True)
    trans_status=models.CharField(max_length=255)
    payment_method=models.CharField(max_length=255)
    pay_status=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.customer