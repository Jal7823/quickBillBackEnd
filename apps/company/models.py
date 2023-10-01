from django.db import models


class Company(models.Model):
    """Model definition for Company."""

    name = models.CharField('Company', max_length=100)
    cuil = models.IntegerField('CUIT')
    cuit = models.IntegerField('CUIL')
    address = models.CharField('Address', max_length=200)
    image = models.ImageField('Image', upload_to='logos/', default='logos/LogoDefault.png')
    phone = models.IntegerField('Phone')

    class Meta:
        """Meta definition for Company."""

        verbose_name = 'Company'
        verbose_name_plural = 'Companys'

    def __str__(self):
        """Unicode representation of Company."""
        return self.name
