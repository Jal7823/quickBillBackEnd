from django.http import request

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema

from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.views.defaults import page_not_found

@extend_schema(
    request={
        "type": "object",
  "properties": {
    "name": {"type": "string"},
    "email": {"type": "string"},
    "order": {"type": "string"},
    "message": {"type": "string"}
  },
  "required": ["name", "email", "order", "message"]
    },
    responses={200: 'Email was sent successfully'}
)
@api_view(['POST'])
def send_order(request,name,email,order,message):
    """
    This function sends an email using data submitted via a POST request.

    Parameters:
    request (HttpRequest): The HTTP request object containing the data to be sent in the email.

    Returns:
    Response: A response object containing a message indicating whether or not the email was sent successfully.

    Raises:
    N/A

    Usage:
    This function is designed to be used as a view in a Django Rest Framework API.

    Example:
    POST /send_order/
    {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "order": "12345",
        "message": "I have a question about my order"
    }

    Response:
    HTTP 200 OK
    "Email was sent successfully"
    """
    if request.method == 'POST':
        name = request.data.get('name')
        email = request.data.get('email')
        order = request.data.get('order')
        message =request.data.get('message')

        template = render_to_string(
            'email.html',{
                'name':name,
                'email':email,
                'order':order,
                'message':message
            }
        )

        email = EmailMessage(
            email,
            template,
            settings.EMAIL_HOST_USER,
            ['jal7823@gmail.com']
        )

        email.fail_silently = False
        email.send()

        msg = 'Email was sent successfully'

        return Response(msg,status=status.HTTP_200_OK)