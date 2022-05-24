from django.contrib.auth.models import User, Group
from rest_framework import serializers
from seshat.apps.crisisdb.models import Famine_event, Land_yield, Total_tax, Total_revenue, Salt_tax
from .models import Album
from ..core.models import Polity, Reference


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ['id', 'title', 'year', 'creator', 'zotero_link', 'long_name']


# class FamineSerializer(serializers.ModelSerializer):
#     politys = serializers.HyperlinkedIdentityField(read_only=True)

#     class Meta:
#         model = Famine_event
#         fields = ('longitude', 'latitude', 'elevation', 'politys')

class Total_taxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total_tax
        fields = ['year_from', 'year_to', 'total_amount_of_taxes_collected']


class Total_revenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total_revenue
        fields = ['year_from', 'year_to', 'total_revenue']


class Salt_taxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salt_tax
        fields = ['year_from', 'year_to', 'salt_tax']


class PolitySerializer(serializers.ModelSerializer):
    #crisisdb_gdp_per_capita_related = serializers.StringRelatedField(many=True,)
    crisisdb_total_tax_related = Total_taxSerializer(many=True, read_only=True)
    crisisdb_salt_tax_related = Salt_taxSerializer(many=True, read_only=True)
    crisisdb_total_revenue_related = Total_revenueSerializer(
        many=True, read_only=True)

    class Meta:
        model = Polity
        fields = ['id', 'name', 'start', 'end',
                  'crisisdb_total_tax_related', 'crisisdb_salt_tax_related', 'crisisdb_total_revenue_related']

#     def create(self, validated_data):
#         return Polity.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.Famines = validated_data
#         return instance


# class FullPolitySerializer(serializers.ModelSerializer):
#     politys = PolitySerializer(source='salt_tax_related')

#     class Meta:
#         model =


class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']
