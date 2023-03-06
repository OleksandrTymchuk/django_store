from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def cart_count(context):
    request = context["request"]
    if request.session.get("products", False):
        return len(request.session.get("products"))
    return 0