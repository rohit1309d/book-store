from django import template
from books.models import Order

register = template.Library()


@register.filter
def rtn_item_count(user):
    if user.is_authenticated:
        qs = orders = Order.objects.filter(ordered=True,return_started = True,returned = False)
        if qs.exists():
            return qs[0].items.count()
    return 0