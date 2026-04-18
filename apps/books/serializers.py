from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        request = self.context.get('request')

        # Automatically assign logged-in user
        if request and request.user:
            validated_data['user'] = request.user

        return super().create(validated_data)