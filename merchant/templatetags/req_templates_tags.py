from django import template
from books.models import Order

register = template.Library()


@register.filter
def req_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(ordered=True,delivered = False,mer = False)
        if qs.exists():
            return qs[0].items.count()
    return 0