from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the use object"""
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'firstName', 'lastName')
        extra_kwargs = {'password': {'write_only': True, 'min_length':5}}

    def create(self, validated_data):
        """Create new user with encrypted password and return it"""
        # UserProfile.objects.create(user=user, dob=dob_data)
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):  #instance is model instance linked to our model object User,
        #validated_data is the fields above
        """Update the user, setting the password correctly and return it"""
        password = validated_data.pop('password', None) #remove password from validated data, None is just default param for required field
        user = super().update(instance, validated_data) #access functions of ModelSerializer class

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs



