from basketapp.models import Basket

def basket(request):
    print(f'context processor basket works')
    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    return {"basket": basket,}


def menu_links(request):
    return {
        "menu_links": [
            {"url": "main", "active": ["main"], "name": "домой"},
            {
                "url": "products:all",
                "active": ["products:all", "products:category"],
                "name": "продукты",
            },
            {"url": "contact", "active": ["contact"], "name": "контакты"},
        ]
    }
