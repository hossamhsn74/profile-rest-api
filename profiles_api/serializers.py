from rest_framework import serializers
from profiles_api.models import UserProfile, ProfileFeedItem


class HelloApiSerializer(serializers.Serializer):
    """ Serializer for name field to test ApiView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializer for user profile object """
    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """
        create and return a user
        """
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
