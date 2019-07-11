from rest_framework import serializers

from . import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects"""

    # define a meta class that tells django what field we what want to take from our model
    class Meta:
        # Assign the model its going to point to
        model = models.UserProfile
        # What fields we want to use in our serializer
        fields = ('id', 'email', 'name', 'password')
        # keyword args for our model (allows us to tell django rest framework special attrs we want to apply to fields)
        # password field should be write only
        extra_kwargs = {'password': {'write_only': True}}

    # function overwrites the create functionality
    def create(self, validated_data):
        """Create and return a new user"""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileFeedSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items"""

    class Meta:
        """tells django what field to take from our model"""
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        # set user_profile as read only automatically, so a user can't create feeds for other users.
        # create a profile feed item for the currently logged in user.
        extra_kwargs = {'user_profile': {'read_only': True}}
