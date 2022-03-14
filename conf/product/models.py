from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name=_('product name'), db_index=True)
    description = models.TextField(verbose_name=_('product description'))
    price = models.PositiveBigIntegerField(default=0, )
    is_active = models.BooleanField(default=False)

    def comment(self):
        return self.comments.filter(active=True)

    def __str__(self):
        return self.name
