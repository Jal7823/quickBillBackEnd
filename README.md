:rocket:  ## QuickBillBackEnd
QuickBillBackEnd is the backend for the QuickBill project, an application to manage sales and invoices. It's built with Django Rest Framework and uses SimpleJWT for authentication.

:computer: ### Getting Started
To get started with QuickBillBackEnd, you need to have Python 3 and Django installed on your machine. Clone the repository and install the required dependencies with the following commands:

bash
Copy code
git clone https://github.com/Jal7823/quickBillBackEnd.git
cd quickBillBackEnd
pip install -r requirements.txt
Once the dependencies are installed, you can start the development server with the following command:

bash
Copy code
python manage.py runserver
You should now be able to access the QuickBillBackEnd API at http://localhost:8000/api/.

:shield: ### Authentication
QuickBillBackEnd uses SimpleJWT for authentication. To obtain an access token, you need to make a POST request to the /api/token/ endpoint with valid credentials. The response will include an access token and a refresh token, which you can use to authenticate requests to protected endpoints.

:lock: ### Authorization
QuickBillBackEnd has several protected endpoints that require authorization. The available permissions are:

IsAdminUser: Only users with the is_staff flag set to True can access the endpoint.
IsEmploye: Only users with the is_employe flag set to True can access the endpoint.
IsBoss: Only users with the is_boss flag set to True can access the endpoint.
To access a protected endpoint, you need to include an Authorization header in your request with the value Bearer <access_token>.

:vertical_traffic_light: ### Testing
QuickBillBackEnd comes with a set of unit tests to ensure that the API works as expected. You can run the tests with the following command:

bash
Copy code
python manage.py test

:handshake: ### Contributing
Contributions are welcome! If you find a bug or want to add a new feature, feel free to open an issue or submit a pull request.

:notebook_with_decorative_cover: ### License
QuickBillBackEnd is licensed under the MIT License. See LICENSE for more information.