import django_filters

from .models import Customer


class CustomerFilter(django_filters.FilterSet):  # Stockfilter used to filter based on name
    uid = django_filters.CharFilter(lookup_expr='icontains')  # allows filtering without entering the full name

    class Meta:
        model = Customer
        fields = ['uid']
