from rest_framework.response import Response
from rest_framework.views import APIView

from .tasks import send_activation_email


class UserActivateView(APIView):
    def post(self, request):
        email = request.data.get('email')
        activation_link = request.data.get('activation_link')

        send_activation_email.delay(email, activation_link)

        return Response({'message': 'Activation email sent successfully.'})
