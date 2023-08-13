from rest_framework import serializers
from searchapp.models import SearchInput


class CustomInputValueSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = SearchInput
        fields = ('timestamp', 'input_values')
