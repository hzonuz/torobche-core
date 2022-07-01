from django.urls import path

from report.views import ReportListView, CreateReportView

app_name = 'report'
urlpatterns = [
    path('v0/', ReportListView.as_view(), name='report'),
    path('<product_id>/v0/', CreateReportView.as_view(), name='create-report-v0')
]