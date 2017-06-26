from django import template

register = template.Library()

## isntead of register.filter('cut',cut), you can do:
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of 'arg' from the string!
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
