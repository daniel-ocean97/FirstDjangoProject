from django import template

register = template.Library()


@register.filter(name='media_filter')
def media_filter(path):
    if path:
        return f"/media/{path}"
    return "#'"