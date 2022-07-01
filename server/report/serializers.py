from rest_framework import serializers

from report.models import Report

class ReportSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Report
        fields = ['id', 'product', 'user', 'description', 'reason']

class CreateReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['description', 'reason']