from django import template
from django.db.models import Q

from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("menu_items_nav.html", takes_context=True)
def all_menu_items(context):
    request = context['request']
    if request.user.is_authenticated:
        return {"all_menu_items_list": MenuItem.objects.order_by("-id")}
    else:
        return {"all_menu_items_list": MenuItem.objects.filter(~Q(url='/products/add'),
                                                               ~Q(url='/products/category/add'))}