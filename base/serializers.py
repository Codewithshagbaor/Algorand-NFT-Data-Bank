# serializers.py
from rest_framework import serializers
from algosdk import account, encoding

class DocumentUploadSerializer(serializers.Serializer):
    document = serializers.FileField()
    user_wallet_address = serializers.CharField()

    def validate(self, data):
        if not data['document'].name.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            raise serializers.ValidationError("We only support images at the moment.")
        if not data['user_wallet_address']:
            raise serializers.ValidationError("The user's wallet address is required.")
        user_wallet_address = data['user_wallet_address']
        if encoding.is_valid_address(user_wallet_address):
            return data
        else:
            raise serializers.ValidationError("The address is invalid.")
