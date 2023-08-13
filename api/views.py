from rest_framework import generics, permissions
from searchapp.models import SearchInput
from .serializers import CustomInputValueSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication


class InputValueListCreateAPIView( generics.ListCreateAPIView):
    queryset = SearchInput.objects.all()
    serializer_class = CustomInputValueSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        user_id = request.user.id
        queryset = self.filter_queryset(
            self.get_queryset().filter(user_id=user_id))
        # queryset = SearchInput.objects.all()

        serializer = CustomInputValueSerializer(queryset, many=True)

        response_data = {
            "status": "success",
            "user_id": user_id,
            "payload": serializer.data
        }

        return Response(response_data, status=status.HTTP_200_OK)


class InputValueRetrieveUpdateDestroyAPIView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = SearchInput.objects.all()
    serializer_class = CustomInputValueSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
