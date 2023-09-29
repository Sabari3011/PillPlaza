from django.db import models
import datetime
import os
from django.contrib.auth.models import User

# Create your models here.

def getCategoryFileName(req,filename):
    time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    newfilename="%s%s"%(time,filename)
    return os.path.join("categoryImages/",newfilename)

def getProductFileName(req,filename):
    time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    newfilename="%s%s"%(time,filename)
    return os.path.join("productImages/",newfilename)

def getPrescriptionCartFileName(req,filename):
    time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    newfilename="%s%s"%(time,filename)
    return os.path.join("Temperary/",newfilename)

def getguestPrescriptionCartFileName(req,filename):
    time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    newfilename="%s%s"%(time,filename)
    return os.path.join("guestpriscription/",newfilename)

class Category(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    image=models.ImageField(upload_to=getCategoryFileName,null=False,blank=False)
    description=models.TextField(max_length=150,null=False,blank=False)
    statusHide=models.BooleanField(default=False,help_text="1-hide , 0-display")
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
    
class Product(models.Model):
    badge=(
        ('Trending','Trending'),
        ('New Arrivals','New Arrivals'),
        ('Top Selling','Top Selling')
    )
    name=models.CharField(max_length=50,null=False,blank=False)
    category_type=models.ForeignKey(Category, on_delete=models.CASCADE,null=False,blank=False)
    ProductImage=models.ImageField(upload_to=getProductFileName,null=False,blank=False)
    description=models.TextField(max_length=150,null=False,blank=False)
    purpose=models.TextField(max_length=150,null=False,blank=False)
    quantity=models.CharField(max_length=50,null=False,blank=False)
    stock=models.IntegerField(null=False,blank=False)
    statusHide=models.BooleanField(default=False,help_text="1-hide , 0-display")
    superbadge=models.CharField( max_length=50,choices=badge,null=True,blank=True)
    markedprice=models.IntegerField(null=False,blank=False)
    sellingprice=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    ratings=models.FloatField(default=0)
    noofSales=models.IntegerField(default=0)
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-noofSales',)

class Review(models.Model):
    name=models.ForeignKey(User, on_delete=models.CASCADE)
    review=models.TextField(max_length=250,null=False,blank=False)
    ratings=models.IntegerField(default=0)
    product_name=models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.first_name +" For "+ self.product_name.name

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    # def __str__(self):
    #     return str(self.user)

class PrescriptiveCart(models.Model):
    options=(
        ('Approved','Approved'),
        ('Processing','Processing'),
        ('Declined','Declined')
    )
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    PrescriptionImage=models.ImageField(upload_to=getPrescriptionCartFileName,null=False,blank=False)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    approve=models.CharField( max_length=50,choices=options,default=options[2],null=False,blank=False)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

class Orders(models.Model):
    statusoption=(
        (1,'Active'),
        (2,'Dispatched'),
        (3,'Out For Delivery'),
        (4,'Delivered'),
        (5,'Declined')
    )
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    orderid=models.CharField(max_length=100)
    totalprice=models.IntegerField(null=False,blank=False)
    totalproducts=models.IntegerField(null=False,blank=False)
    status=models.IntegerField(choices=statusoption,default=1,null=False,blank=False)
    address=models.TextField(max_length=300) 
    pincode=models.CharField(max_length=6)  
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    review=models.BooleanField(default=False)

    class Meta:
        ordering =('-updated_at',)

class Orderitems(models.Model):
    orderid=models.ForeignKey(Orders, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField(null=False,blank=False)
    review=models.BooleanField(default=False)


class Refund(models.Model):
    orderid=models.ForeignKey(Orders,unique=True, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    refundupi=models.CharField(max_length=50,null=False,blank=False)
    refundAmount=models.IntegerField(null=False,blank=False)
    reason=models.TextField(max_length=250,null=False,blank=False)
    done=models.BooleanField(default= False)

class Guest(models.Model):
    statusoption=(
        (1,'Apply'),
        (2,'Dispatched'),
        (3,'Out For Delivery'),
        (4,'Delivered'),
        (5,'Declined'))
    
    guestname=models.CharField(max_length=100)
    guestid=models.CharField(max_length=100)
    guestPrescriptionImage=models.ImageField(upload_to=getguestPrescriptionCartFileName,null=False,blank=False)
    email=models.CharField( max_length=50,null=False,blank=False)
    mobileno=models.CharField( max_length=50,null=False,blank=False)
    totalprice=models.IntegerField(null=False,blank=False,default=10)
    actualproducts=models.IntegerField(null=False,blank=False,default=0)
    totalproducts=models.IntegerField(null=False,blank=False,default=0)
    status=models.IntegerField(choices=statusoption,default=1,null=False,blank=False)
    address=models.TextField(max_length=300) 
    pincode=models.CharField(max_length=6)  
    agree=models.BooleanField(default= False)
    created_at=models.DateTimeField(auto_now_add=True)


class GuestProducts(models.Model):
    guestid=models.ForeignKey(Guest, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField(null=False,blank=False)
    updated=models.BooleanField(default=False)
    


class Summary(models.Model):
    cash=models.IntegerField(default=0)
    totalcategory=models.IntegerField(default=0)
    totalproducts=models.IntegerField(default=0)
    totalsales=models.IntegerField(default=0)
    guestuser=models.IntegerField(default=0)
    registered_user=models.IntegerField(default=0)


