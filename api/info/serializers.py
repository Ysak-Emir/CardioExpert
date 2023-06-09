from rest_framework import serializers

from api.info.models import CategoryInformation, SubcategoryInformation


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryInformation
        fields = 'id title_rus title_kz'.split()


class SubcategorySerializer(serializers.ModelSerializer):
    block = serializers.SerializerMethodField()

    class Meta:
        model = SubcategoryInformation
        fields = 'id profile_picture title description_rus description_kz block'.split()

    def get_block(self, instance):
        return instance.block.title_rus

