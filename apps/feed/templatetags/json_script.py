from django import template
from django.urls import reverse

register = template.Library()


@register.inclusion_tag('includes/json_script.html')
def json_script(script_id, content):
    return {'script_id': script_id, 'content': content}


@register.inclusion_tag('includes/json_script.html')
def url_json_script(script_id, url_name, *args, **kwargs):
    url = reverse(url_name, args=args, kwargs=kwargs)
    return {'script_id': script_id, 'content': url}
