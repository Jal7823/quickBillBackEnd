from django.db import models


class Provider(models.Model):
    """Model definition for Provider."""

    name = models.CharField('Name', max_length=50)

    class Meta:
        """Meta definition for Provider."""

        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'

    def __str__(self):
        """Unicode representation of Provider."""
        return self.name

class Category(models.Model):
    """Model definition for Category."""

    name = models.CharField('Name', max_length=80)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name

class Brand(models.Model):
    """Model definition for Brand."""

    name = models.CharField('Name', max_length=80)

    class Meta:
        """Meta definition for Brand."""

        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        """Unicode representation of Brand."""
        return self.name

class Products(models.Model):
    code = models.IntegerField('Internal Code')
    name = models.CharField('Name', max_length=80)
    description = models.TextField('Description',blank=True,null=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE,null=True,blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,null=True,blank=True)
    category = models.ManyToManyField(Category)
    price = models.FloatField('Price')
    wPrice = models.IntegerField("wholesaler's price")
    image = models.ImageField('Image', upload_to='products',null=True,blank=True,default='products/defaultProduct.png')
    stock = models.IntegerField('Stock')
    created = models.DateField(auto_now_add=True, verbose_name='Created')
    updated = models.DateField(auto_now_add=True, verbose_name='Updated')

    def __str__(self):
        return self.name
    
    class Meta:
        """Meta definition for Products."""

        verbose_name = 'Products'
        verbose_name_plural = 'Productss'

