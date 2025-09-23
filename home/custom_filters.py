# home/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def filter_created_for(queryset, user):
    """Filter queryset by created_for field"""
    try:
        return queryset.filter(created_for=user)
    except:
        return queryset.none()