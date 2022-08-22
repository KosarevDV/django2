# Generated by Django 3.2.9 on 2022-08-21 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0002_auto_20220821_0019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('created',), 'verbose_name': 'заказ', 'verbose_name_plural': 'заказы'},
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='создан'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('FM', 'формируется'), ('STP', 'отправлен в обработку'), ('PRD', 'обрабатывается'), ('PD', 'оплачен'), ('RDY', 'готов к выдаче'), ('CNC', 'отменен')], default='FM', max_length=3, verbose_name='статус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='обновлен'),
        ),
    ]