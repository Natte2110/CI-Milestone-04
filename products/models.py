from django.db import models

# Create your models here.
from django.utils.text import slugify

class Brand(models.Model):
    """
    Class to determine the brands of products available
    """
    name=models.CharField(max_length=100, unique=True, null=False)
    image_url=models.URLField(max_length=2000, null=True, blank=True)
    image=models.ImageField(null=True, blank=True)
    is_featured=models.BooleanField(default=False)


class Category(models.Model):
    """
    Class to define the Category Model
    """
    name=models.CharField(max_length=100, unique=True, null=False)


class Product(models.Model):
    """
    Class to define the products themselves
    """
    category=models.ForeignKey('Category', on_delete=models.CASCADE)
    brand=models.ForeignKey('Brand', on_delete=models.CASCADE)
    sku=models.CharField(max_length=32, null=False, unique=True)
    name=models.CharField(max_length=32, null=False, unique=True)
    description=models.TextField(max_length=3000, null=False, blank=False)
    available_quanitity=models.IntegerField(null=False, blank=False)
    price=models.DecimalField(null=False, blank=False)
    is_discounted=models.BooleanField(default=False)
    discount_price=models.DecimalField(null=False, blank=False)
    is_featured=models.BooleanField(default=False)
    image_url=models.URLField(max_length=2000, null=True, blank=True)
    image=models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=250, null=False, unique=True,
                            blank=False,)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class CPUSocket():
    '''
    Class to define the type of CPU used
    '''
    socket_type=models.CharField(max_length=32, null=False, blank=False)


class RAMTechnology():
    '''
    Class to define the technology used for a components RAM
    '''
    technology_style=models.CharField(max_length=32, null=False, blank=False)


class FormFactor():
    '''
    Class to define the form factor of a component
    '''
    style_name=models.CharField(max_length=32, null=False, blank=False)


class Motherboard(Product):
    '''
    Class to define extra product information for motherboards
    '''
    form_factor=models.ForeignKey('FormFactor', on_delete=models.CASCADE)
    ram_technology=models.ForeignKey('RAMTechnology', on_delete=models.CASCADE)
    cpu_socket=models.ForeignKey('CPUSocket', on_delete=models.CASCADE)
    memory_clock_speed=models.DecimalField(null=False, blank=False)


class CPU(Product):
    '''
    Class to define product information for CPU's
    '''
    cpu_socket=models.ForeignKey('CPUSocket', on_delete=models.CASCADE)
    cpu_speed=models.DecimalField(null=False, blank=False)
    secondary_cache=models.IntegerField(null=False, blank=False)
    cache=models.IntegerField(null=False, blank=False)
    wattage=models.IntegerField(null=False, blank=False)
    processor_count=models.IntegerField(null=False, blank=False)
    cores=models.IntegerField(null=False, blank=False)


class RAM(Product):
    '''
    Class to define extra product information for RAM
    '''
    ram_technology=models.ForeignKey('RAMTechnology', on_delete=models.CASCADE)
    memory_size=models.IntegerField(null=False, blank=False)
    no_sticks=models.IntegerField(null=False, blank=False)
    memory_speed=models.DecimalField(null=False, blank=False)


class PSU(Product):
    '''
    Class to define extra product information for power supplies
    '''
    form_factor=models.ForeignKey('FormFactor', on_delete=models.CASCADE)
    wattage=models.IntegerField(null=False, blank=False)


class GPU(Product):
    '''
    Class to define extra product information for GPU's
    '''
    g_ram_technology=models.CharField(max_length=32, null=False, blank=False)
    clock_speed=models.IntegerField(null=False, blank=False)
    g_ram_size=models.IntegerField(null=False, blank=False)
    video_interface=models.CharField(max_length=32, null=False, blank=False)