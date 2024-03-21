from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.utils import timezone

# class CustomUser(AbstractUser):
#     is_vendor=models.BooleanField(default=False)

class ProductDetails(models.Model):
    Pvendorname = models.OneToOneField(User, on_delete=models.CASCADE) #vendors username
    Pname = models.CharField(max_length=100)
    Ppicture = models.ImageField(upload_to='product_picture', null=True,blank=True)
    Pdesc = models.CharField(max_length=1000)
    Pstock = models.IntegerField()
    Pprice = models.IntegerField()
    Pmallname = models.CharField(max_length=100)
    Pcatg = models.CharField(max_length=100)
    product_code = models.CharField(max_length=15, unique=True, editable=False)  # Custom product code field

    def save(self, *args, **kwargs):
        if not self.pk:  # If the instance is being created (not updated)
            last_product = ProductDetails.objects.filter(Pvendorname=self.Pvendorname).order_by('-id').first()
            if last_product:
                last_id = int(last_product.id)  # Assuming format is 'EMPXXX'
                self.product_code = 'PC{:03d}'.format(last_id + 1)
            else:
                self.product_code = 'PC001'
        super().save(*args, **kwargs)  


class cartProductitems(models.Model):
    username = models.CharField(max_length=100)
    CPname = models.CharField(max_length=150)
    CPpicture = models.ImageField(upload_to='cart_picture', null=True,blank=True)
    ProductID = models.IntegerField()
    CPrice = models.IntegerField() 

class PurchesDetails(models.Model):
    username= models.CharField(max_length=100) #its usernamer of buyer
    PPname= models.CharField(max_length=100) #it is products vendor name not product name
    PPid = models.IntegerField() #main products id
    Pfirstname= models.CharField(max_length=100)
    Plastname= models.CharField(max_length=100)
    Pmobile = models.IntegerField()
    Pemail =models.EmailField()
    Padderss= models.CharField(max_length=100)
    Pzipcode = models.IntegerField()
    Pdivision= models.CharField(max_length=100)
    Pcity= models.CharField(max_length=100)
    Parea= models.CharField(max_length=100)
    Pdeliverytyp= models.CharField(max_length=100)
    quantity = models.IntegerField()
    product_code = models.CharField(max_length=15, editable=False)  # Custom product code field
    confirmation = models.BooleanField(default=False)
    PurchesTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        conf = self.confirmation
        if conf == True:       
            return "confiremed"
        else:
            return "Not Confirmed"

class Catagory(models.Model):
    CatagoryName = models.CharField(max_length=150)