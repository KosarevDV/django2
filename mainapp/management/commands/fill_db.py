import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory

# JSON_PATH = "mainapp/json"
#
#
# def load_from_json(file_name):
#     with open(os.path.join(JSON_PATH, file_name + ".json"), "r", encoding="utf-8") as infile:
#         return json.load(infile)
#
#
# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
#         ProductCategory.objects.all().delete()
#         categories = load_from_json("categories")
#         for category in categories:
#             new_category = ProductCategory(**category)
#             new_category.save()
#
#         Product.objects.all().delete()
#         products = load_from_json("products")
#
#         for product in products:
#             category_name = product["category"]
#             # Получаем категорию по имени
#             category = ProductCategory.objects.get(name=category_name)
#             # Заменяем название категории объектом
#             product["category"] = category
#             new_product = Product(**product)
#             new_product.save()
#
#         # Создаем суперпользователя при помощи менеджера модели
#         ShopUser.objects.create_superuser(
#             "admin", "admin@localhost", "123"
#        )
class Command(BaseCommand):

    @staticmethod
    def _load_data_from_file(file_name):
        with open(f'{settings.BASE_DIR}/mainapp/json/{file_name}.json', encoding="utf-8") as json_file:
            json_string = json_file.read()
            return json.loads(json_string)
            #return json.load(json_file)


    def handle(self, *args, **options):
        ProductCategory.objects.all().delete()
        categories_list = self._load_data_from_file('categories')
        print(categories_list)
        categories_batch = []
        for cat in categories_list:
            categories_batch.append(ProductCategory(name=cat.get('name'), description=cat.get('description')))

        ProductCategory.objects.bulk_create(categories_batch)

        Product.objects.all().delete()
        products_list = self._load_data_from_file('products')
        for prod in products_list:
            _cat = ProductCategory.objects.filter(name=prod.get('category')).first()
            prod['category'] = _cat
            Product.objects.create(**prod)

        ShopUser.objects.create_superuser(
            "admin", "admin@localhost", "123")

