from apps.products.models import Products

def populateProducts():
    for i in range(200):
        a = Products.objects.create(
            code=i,
            name=f'Name of Product {i}',
            description=f'Description of Product {i}',
            price=i*5,

            wPrice=(i*5*20)/100,
            image='http://localhost:8000/media/products/LogoDefault.png',
            stock=i,
        )
        a.save()
        print(f'product {i} was register successfully')
    print('<========= end script ============>')

