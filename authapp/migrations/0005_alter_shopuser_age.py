# Generated by Django 4.1 on 2022-08-13 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_alter_shopuser_age_shopuserprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(blank=True, verbose_name='возраст'),
        ),
    ]
