from django_filters import FilterSet, ModelMultipleChoiceFilter

from apps.models import Order, Region, Category, District


class OrderFilterSet(FilterSet):
    category = ModelMultipleChoiceFilter(field_name='product__category', queryset=Category.objects.all(), label='Category')
    region = ModelMultipleChoiceFilter(field_name='district__region', queryset=Region.objects.all(), label='Region')
    district = ModelMultipleChoiceFilter(queryset=District.objects.all(), label='District')

    def filter_queryset(self, queryset):
        query =  super().filter_queryset(queryset)
        if self.data.get('status') != 'all':
            query = query.filter(status = self.data.get('status'))
        return query
    class Meta:
        model = Order
        fields = ['category', 'region', 'district']
