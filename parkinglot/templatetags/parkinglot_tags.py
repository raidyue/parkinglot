from django import template

register = template.Library()


@register.filter(name='page_range')
def page_range(page_count):
    return range(page_count+1)[1:(page_count + 1)]