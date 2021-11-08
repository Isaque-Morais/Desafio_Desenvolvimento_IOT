from django.db import models
from django.utils.translation import gettext_lazy as _

class tipo_nota(models.TextChoices):
        CUPOM_FISCAL = 'CUPO', _('Cupom Fiscal')
        NOTA_FISCAL = 'NOTA', _('Nota Fiscal')