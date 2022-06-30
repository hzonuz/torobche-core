from rest_framework import filters

from product.models import Category

class FilterCategories(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        category = request.query_params.get('category', None)

        if category:
            queryset = queryset.filter(category__in=Category.objects.get(id=category).get_descendants(include_self=True))

        return queryset