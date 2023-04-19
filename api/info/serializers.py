from rest_framework import serializers

from api.info.models import CategoryInformation, SubcategoryInformation


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryInformation
        fields = 'id title'.split()


class SubcategorySerializer(serializers.ModelSerializer):
    block = serializers.SerializerMethodField()

    class Meta:
        model = SubcategoryInformation
        fields = 'id profile_picture title description block'.split()

    def get_block(self, instance):
        return instance.block.title


    # def get_block_title_name(self, obj):
    #     return obj.CategoryInformation.title

    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['block_title'] = instance.block_title
    #     return ret

    # @staticmethod
    # def get_block_title(instance):
    #     return instance.block_title.block_title
