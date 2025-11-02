from django.db import models
from django.utils.translation import gettext as _


class Service(models.Model):


    name = models.CharField(("نام وبسایت"), max_length=20) 
    short_discription = models.TextField((" توضیحات کوتاه "), max_length=100, null=True, blank=True)
    long_discription = models.TextField((" توضیحات بلند "), null=True, blank=True)
    category = models.CharField(("دسته بندی"), max_length=20)
    lable = models.ImageField(("پوستر"),upload_to='image/', null=True, blank=True)
    link = models.CharField(("لینک"),max_length=50)
    frontend = models.CharField(max_length=100, null=True, blank=True)
    backend = models.CharField(max_length=100, null=True, blank=True) 
    hosting = models.CharField(max_length=100, null=True, blank=True)
    authentication = models.CharField(max_length=100, null=True, blank=True)
    delivery_time = models.CharField(max_length=100, null=True, blank=True)
    pagespeed = models.DecimalField(max_digits=5,decimal_places=3,  null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    image_1 = models.ImageField(('تصویر'), upload_to='image/', null=True, blank=True)
    image_2 = models.ImageField(('تصویر'), upload_to='image/', null=True, blank=True)
    image_3 = models.ImageField(('تصویر'), upload_to='image/', null=True, blank=True)
    image_4 = models.ImageField(('تصویر'), upload_to='image/', null=True, blank=True)
    image_5 = models.ImageField(('تصویر'), upload_to='image/', null=True, blank=True)
    image_6 = models.ImageField(('تصویر'), upload_to='image/', null=True, blank=True)
    image_7 = models.ImageField(('تصویر'), upload_to='image/', null=True, blank=True)
    image_8 = models.ImageField(('تصویر'), upload_to='image/', null=True, blank=True)

