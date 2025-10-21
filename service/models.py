from django.db import models
from django.utils.translation import gettext as _


class Service(models.Model):


    name = models.CharField(("نام وبسایت"), max_length=20) 
    discription = models.TextField(("توضیحات"), max_length=300)
    category = models.CharField(("دسته بندی"), max_length=20)
    lable = models.ImageField(("پوستر"),upload_to='image/', null=True, blank=True)
    link = models.CharField(("لینک"),max_length=50)
    

