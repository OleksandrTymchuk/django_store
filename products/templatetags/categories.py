from django import template
from products.models import Category

register = template.Library()

@register.inclusion_tag("category_nav.html")
def all_categories():
    return {"all_categories_list":Category.objects.filter(parent_id=None).order_by("-id")}