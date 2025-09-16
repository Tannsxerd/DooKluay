from rest_framework import serializers
from ..models import ModelFile

class ModelSerializer(serializers.ModelSerializer):
    # file_url is read-only, generated from the file_path field
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = ModelFile
        fields = '__all__'