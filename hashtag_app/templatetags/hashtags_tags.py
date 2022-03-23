from django import template
from ..models import HashTag
from django.db.models import Count

register = template.Library()


@register.inclusion_tag('hashtags_cloud.html')
def hashtags_cloud():
    return {'tags': HashTag.objects.all().annotate(cnt=Count('post')).order_by('-cnt')}
