from django import template

register = template.Library()


@register.filter(name='addclass')
def adclass(value, arg):
    return value.as_widget(attrs={'class': arg})