from django import template
import pprint
pp = pprint.PrettyPrinter(indent=4)

register = template.Library()

@register.filter(is_safe=True, name='form_label_with_classes')
def form_label_with_classes(tag, arg):
    return tag.label_tag(attrs={'class': arg })

@register.filter(is_safe=True, name='add_class')
def add_class(tag, arg):
    return tag.as_widget(attrs={'class': arg })