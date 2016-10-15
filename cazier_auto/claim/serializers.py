from django.contrib.auth.models import User, Group
from rest_framework import serializers
from cazier_auto.claim.models import Claim


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ClaimSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    series = serializers.CharField(max_length=30)

    def create(self, validated_data):
        """
        Create and return a new `Claim` instance, given the validated data.
        """
        return Claim.objects.create(**validated_data)

    class Meta:
        model = Claim
        fields = ('id', 'created', 'series', 'user',)
