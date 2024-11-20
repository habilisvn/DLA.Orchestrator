"""
This type stub file was generated by pyright.
"""

from mongoengine.queryset.queryset import QuerySet

__all__ = ("queryset_manager", "QuerySetManager")
class QuerySetManager:
    """
    The default QuerySet Manager.

    Custom QuerySet Manager functions can extend this class and users can
    add extra queryset functionality.  Any custom manager methods must accept a
    :class:`~mongoengine.Document` class as its first argument, and a
    :class:`~mongoengine.queryset.QuerySet` as its second argument.

    The method function should return a :class:`~mongoengine.queryset.QuerySet`
    , probably the same one that was passed in, but modified in some way.
    """
    get_queryset = ...
    default = QuerySet
    def __init__(self, queryset_func=...) -> None:
        ...
    
    def __get__(self, instance, owner): # -> Self | partial[Any]:
        """Descriptor for instantiating a new QuerySet object when
        Document.objects is accessed.
        """
        ...
    


def queryset_manager(func): # -> QuerySetManager:
    """Decorator that allows you to define custom QuerySet managers on
    :class:`~mongoengine.Document` classes. The manager must be a function that
    accepts a :class:`~mongoengine.Document` class as its first argument, and a
    :class:`~mongoengine.queryset.QuerySet` as its second argument. The method
    function should return a :class:`~mongoengine.queryset.QuerySet`, probably
    the same one that was passed in, but modified in some way.
    """
    ...

