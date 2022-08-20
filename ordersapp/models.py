from django.conf import settings
from django.db import models


class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = "CNC"

    ORDER_STATUS_CHOICES = (
        (FORMING, "формируется"),
        (SENT_TO_PROCEED, "отправлен в обработку"),
        (PROCEEDED, "обрабатывается"),
        (PAID, "оплачен"),
        (READY, "готов к выдаче"),
        (CANCEL, "отменен"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateField(verbose_name='создан', auto_now_add=True)
    updated = models.DateField(verbose_name='обновлен', auto_now=True)
    is_active = models.BooleanField(verbose_name='активен', default=True)

    status = models.CharField(verbose_name='статус', max_length=128, choices=ORDER_STATUS_CHOICES, default=FORMING)

    class Meta:
        ordering = ('created',)
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f'Текущий заказ: {self.id} '
