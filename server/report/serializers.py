from rest_framework import serializers

from report.models import Report
from user.serializers import UserSerializer

class ReportSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    product = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Report
        fields = ['id', 'product', 'user', 'description', 'reason']

class CreateReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['description', 'reason']