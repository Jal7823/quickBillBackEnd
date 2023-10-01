from apps.users.models import Users
from faker import Faker
import hashlib

faker = Faker()


def populateUsers():
    for i in range(10):
        password = faker.password()  # Generar una contraseña aleatoria
        password_hash = hashlib.sha256(password.encode()).hexdigest() 
        
        a = Users.objects.create(
            username=faker.name(),
            name=faker.name(),
            email=faker.email(),
            password=password_hash,
            image='http://localhost:8000/media/products/LogoDefault.png',
            is_staff=False,
            is_employe=False,
            is_boss=False,
            address=faker.address(),
            location=faker.name(),
            province=faker.name(),
            phone=1111111,
        )
        a.save()
        print(f'user {a.name} was registered successfully')
    
    print('<========= end script ============>')


populateUsers()