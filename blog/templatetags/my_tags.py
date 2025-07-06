from django import template

register = template.Library()  # Скобки () обязательны!


@register.filter(name="media_filter")  # Явное указание имени
def media_filter(path):
    if path:
        return f"/media/{path}"
    return "#"
