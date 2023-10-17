from rest_framework import serializers
from .models import Scanner, Entry

class ScannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scanner
        fields = '__all__'

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'

