from apps.products.models import Products

def populateProducts():
    for i in range(20):
        a = Products.objects.create(
            code=i,
            name=f'Product example nro. {i}',
            description=f"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type",
            price=i*2,
            image='http://localhost:8000/media/products/LogoDefault.png',
            stock=i,
        )
        a.save()
        print(f'product {i} was register successfully')
    print('<========= end script ============>')

