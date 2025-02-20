"""
This type stub file was generated by pyright.
"""

from mongoengine.base import BaseField, ComplexBaseField, GeoJsonBaseField
from PIL import Image

if hasattr(Image, "Resampling"):
    LANCZOS = ...
else:
    LANCZOS = ...
__all__ = ("StringField", "URLField", "EmailField", "IntField", "LongField", "FloatField", "DecimalField", "BooleanField", "DateTimeField", "DateField", "ComplexDateTimeField", "EmbeddedDocumentField", "ObjectIdField", "GenericEmbeddedDocumentField", "DynamicField", "ListField", "SortedListField", "EmbeddedDocumentListField", "DictField", "MapField", "ReferenceField", "CachedReferenceField", "LazyReferenceField", "GenericLazyReferenceField", "GenericReferenceField", "BinaryField", "GridFSError", "GridFSProxy", "FileField", "ImageGridFsProxy", "ImproperlyConfigured", "ImageField", "GeoPointField", "PointField", "LineStringField", "PolygonField", "SequenceField", "UUIDField", "EnumField", "MultiPointField", "MultiLineStringField", "MultiPolygonField", "GeoJsonBaseField", "Decimal128Field")
RECURSIVE_REFERENCE_CONSTANT = ...
class StringField(BaseField):
    """A unicode string field."""
    def __init__(self, regex=..., max_length=..., min_length=..., **kwargs) -> None:
        """
        :param regex: (optional) A string pattern that will be applied during validation
        :param max_length: (optional) A max length that will be applied during validation
        :param min_length: (optional) A min length that will be applied during validation
        :param kwargs: Keyword arguments passed into the parent :class:`~mongoengine.BaseField`
        """
        ...
    
    def to_python(self, value): # -> str:
        ...
    
    def validate(self, value): # -> None:
        ...
    
    def lookup_member(self, member_name): # -> None:
        ...
    
    def prepare_query_value(self, op, value): # -> Pattern[Any | str] | Pattern[Any]:
        ...
    


class URLField(StringField):
    """A field that validates input as an URL."""
    _URL_REGEX = ...
    _URL_SCHEMES = ...
    def __init__(self, url_regex=..., schemes=..., **kwargs) -> None:
        """
        :param url_regex: (optional) Overwrite the default regex used for validation
        :param schemes: (optional) Overwrite the default URL schemes that are allowed
        :param kwargs: Keyword arguments passed into the parent :class:`~mongoengine.StringField`
        """
        ...
    
    def validate(self, value): # -> None:
        ...
    


class EmailField(StringField):
    """A field that validates input as an email address."""
    USER_REGEX = ...
    UTF8_USER_REGEX = ...
    DOMAIN_REGEX = ...
    error_msg = ...
    def __init__(self, domain_whitelist=..., allow_utf8_user=..., allow_ip_domain=..., *args, **kwargs) -> None:
        """
        :param domain_whitelist: (optional) list of valid domain names applied during validation
        :param allow_utf8_user: Allow user part of the email to contain utf8 char
        :param allow_ip_domain: Allow domain part of the email to be an IPv4 or IPv6 address
        :param kwargs: Keyword arguments passed into the parent :class:`~mongoengine.StringField`
        """
        ...
    
    def validate_user_part(self, user_part): # -> Match[str] | None:
        """Validate the user part of the email address. Return True if
        valid and False otherwise.
        """
        ...
    
    def validate_domain_part(self, domain_part): # -> bool:
        """Validate the domain part of the email address. Return True if
        valid and False otherwise.
        """
        ...
    
    def validate(self, value): # -> None:
        ...
    


class IntField(BaseField):
    """32-bit integer field."""
    def __init__(self, min_value=..., max_value=..., **kwargs) -> None:
        """
        :param min_value: (optional) A min value that will be applied during validation
        :param max_value: (optional) A max value that will be applied during validation
        :param kwargs: Keyword arguments passed into the parent :class:`~mongoengine.BaseField`
        """
        ...
    
    def to_python(self, value): # -> int:
        ...
    
    def validate(self, value): # -> None:
        ...
    
    def prepare_query_value(self, op, value): # -> int:
        ...
    


class LongField(IntField):
    """64-bit integer field. (Equivalent to IntField since the support to Python2 was dropped)"""
    def to_mongo(self, value): # -> Int64:
        ...
    


class FloatField(BaseField):
    """Floating point number field."""
    def __init__(self, min_value=..., max_value=..., **kwargs) -> None:
        """
        :param min_value: (optional) A min value that will be applied during validation
        :param max_value: (optional) A max value that will be applied during validation
        :param kwargs: Keyword arguments passed into the parent :class:`~mongoengine.BaseField`
        """
        ...
    
    def to_python(self, value): # -> float:
        ...
    
    def validate(self, value): # -> None:
        ...
    
    def prepare_query_value(self, op, value): # -> float:
        ...
    


class DecimalField(BaseField):
    """Disclaimer: This field is kept for historical reason but since it converts the values to float, it
    is not suitable for true decimal storage. Consider using :class:`~mongoengine.fields.Decimal128Field`.

    Fixed-point decimal number field. Stores the value as a float by default unless `force_string` is used.
    If using floats, beware of Decimal to float conversion (potential precision loss)
    """
    def __init__(self, min_value=..., max_value=..., force_string=..., precision=..., rounding=..., **kwargs) -> None:
        """
        :param min_value: (optional) A min value that will be applied during validation
        :param max_value: (optional) A max value that will be applied during validation
        :param force_string: Store the value as a string (instead of a float).
         Be aware that this affects query sorting and operation like lte, gte (as string comparison is applied)
         and some query operator won't work (e.g. inc, dec)
        :param precision: Number of decimal places to store.
        :param rounding: The rounding rule from the python decimal library:

            - decimal.ROUND_CEILING (towards Infinity)
            - decimal.ROUND_DOWN (towards zero)
            - decimal.ROUND_FLOOR (towards -Infinity)
            - decimal.ROUND_HALF_DOWN (to nearest with ties going towards zero)
            - decimal.ROUND_HALF_EVEN (to nearest with ties going to nearest even integer)
            - decimal.ROUND_HALF_UP (to nearest with ties going away from zero)
            - decimal.ROUND_UP (away from zero)
            - decimal.ROUND_05UP (away from zero if last digit after rounding towards zero would have been 0 or 5; otherwise towards zero)

            Defaults to: ``decimal.ROUND_HALF_UP``
        :param kwargs: Keyword arguments passed into the parent :class:`~mongoengine.BaseField`
        """
        ...
    
    def to_python(self, value): # -> Decimal:
        ...
    
    def to_mongo(self, value): # -> str | float:
        ...
    
    def validate(self, value): # -> None:
        ...
    
    def prepare_query_value(self, op, value): # -> str | float:
        ...
    


class BooleanField(BaseField):
    """Boolean field type."""
    def to_python(self, value): # -> bool:
        ...
    
    def validate(self, value): # -> None:
        ...
    


class DateTimeField(BaseField):
    """Datetime field.

    Uses the python-dateutil library if available alternatively use time.strptime
    to parse the dates.  Note: python-dateutil's parser is fully featured and when
    installed you can utilise it to convert varying types of date formats into valid
    python datetime objects.

    Note: To default the field to the current datetime, use: DateTimeField(default=datetime.utcnow)

    Note: Microseconds are rounded to the nearest millisecond.
      Pre UTC microsecond support is effectively broken.
      Use :class:`~mongoengine.fields.ComplexDateTimeField` if you
      need accurate microsecond support.
    """
    def validate(self, value): # -> None:
        ...
    
    def to_mongo(self, value): # -> datetime | None:
        ...
    
    def prepare_query_value(self, op, value): # -> datetime | None:
        ...
    


class DateField(DateTimeField):
    def to_mongo(self, value): # -> datetime | None:
        ...
    
    def to_python(self, value): # -> date:
        ...
    


class ComplexDateTimeField(StringField):
    """
    ComplexDateTimeField handles microseconds exactly instead of rounding
    like DateTimeField does.

    Derives from a StringField so you can do `gte` and `lte` filtering by
    using lexicographical comparison when filtering / sorting strings.

    The stored string has the following format:

        YYYY,MM,DD,HH,MM,SS,NNNNNN

    Where NNNNNN is the number of microseconds of the represented `datetime`.
    The `,` as the separator can be easily modified by passing the `separator`
    keyword when initializing the field.

    Note: To default the field to the current datetime, use: DateTimeField(default=datetime.utcnow)
    """
    def __init__(self, separator=..., **kwargs) -> None:
        """
        :param separator: Allows to customize the separator used for storage (default ``,``)
        :param kwargs: Keyword arguments passed into the parent :class:`~mongoengine.StringField`
        """
        ...
    
    def __get__(self, instance, owner): # -> Self | datetime:
        ...
    
    def __set__(self, instance, value): # -> None:
        ...
    
    def validate(self, value): # -> None:
        ...
    
    def to_python(self, value): # -> datetime:
        ...
    
    def to_mongo(self, value): # -> str:
        ...
    
    def prepare_query_value(self, op, value): # -> Pattern[Any | str] | Pattern[Any]:
        ...
    


class EmbeddedDocumentField(BaseField):
    """An embedded document field - with a declared document_type.
    Only valid values are subclasses of :class:`~mongoengine.EmbeddedDocument`.
    """
    def __init__(self, document_type, **kwargs) -> None:
        ...
    
    @property
    def document_type(self): # -> type[EmbeddedDocument] | Any | None:
        ...
    
    def to_python(self, value): # -> Self:
        ...
    
    def to_mongo(self, value, use_db_field=..., fields=...): # -> SON[Any, Any]:
        ...
    
    def validate(self, value, clean=...): # -> None:
        """Make sure that the document instance is an instance of the
        EmbeddedDocument subclass provided when the document was defined.
        """
        ...
    
    def lookup_member(self, member_name): # -> None:
        ...
    
    def prepare_query_value(self, op, value): # -> dict[Any, Any] | SON[Any, Any]:
        ...
    


class GenericEmbeddedDocumentField(BaseField):
    """A generic embedded document field - allows any
    :class:`~mongoengine.EmbeddedDocument` to be stored.

    Only valid values are subclasses of :class:`~mongoengine.EmbeddedDocument`.

    .. note ::
        You can use the choices param to limit the acceptable
        EmbeddedDocument types
    """
    def prepare_query_value(self, op, value): # -> None:
        ...
    
    def to_python(self, value):
        ...
    
    def validate(self, value, clean=...): # -> Literal[True] | None:
        ...
    
    def lookup_member(self, member_name): # -> None:
        ...
    
    def to_mongo(self, document, use_db_field=..., fields=...): # -> None:
        ...
    


class DynamicField(BaseField):
    """A truly dynamic field type capable of handling different and varying
    types of data.

    Used by :class:`~mongoengine.DynamicDocument` to handle dynamic data"""
    def to_mongo(self, value, use_db_field=..., fields=...): # -> str | dict[str, DBRef | Any] | list[Any] | dict[Any, Any]:
        """Convert a Python type to a MongoDB compatible type."""
        ...
    
    def to_python(self, value): # -> dict[Any, Any]:
        ...
    
    def lookup_member(self, member_name):
        ...
    
    def prepare_query_value(self, op, value): # -> Pattern[Any | str] | Pattern[Any] | str | dict[str, DBRef | Any] | list[Any] | dict[Any, Any]:
        ...
    
    def validate(self, value, clean=...): # -> None:
        ...
    


class ListField(ComplexBaseField):
    """A list field that wraps a standard field, allowing multiple instances
    of the field to be used as a list in the database.

    If using with ReferenceFields see: :ref:`many-to-many-with-listfields`

    .. note::
        Required means it cannot be empty - as the default for ListFields is []
    """
    def __init__(self, field=..., *, max_length=..., **kwargs) -> None:
        ...
    
    def __get__(self, instance, owner): # -> Self | EmbeddedDocumentList | BaseList | BaseDict | ComplexBaseField:
        ...
    
    def validate(self, value): # -> None:
        """Make sure that a list of valid fields is being used."""
        ...
    
    def prepare_query_value(self, op, value): # -> list[Any | str] | str | BaseDocument | list[Any] | dict[int | Any, Any]:
        ...
    


class EmbeddedDocumentListField(ListField):
    """A :class:`~mongoengine.ListField` designed specially to hold a list of
    embedded documents to provide additional query helpers.

    .. note::
        The only valid list values are subclasses of
        :class:`~mongoengine.EmbeddedDocument`.
    """
    def __init__(self, document_type, **kwargs) -> None:
        """
        :param document_type: The type of
         :class:`~mongoengine.EmbeddedDocument` the list will hold.
        :param kwargs: Keyword arguments passed into the parent :class:`~mongoengine.ListField`
        """
        ...
    


class SortedListField(ListField):
    """A ListField that sorts the contents of its list before writing to
    the database in order to ensure that a sorted list is always
    retrieved.

    .. warning::
        There is a potential race condition when handling lists.  If you set /
        save the whole list then other processes trying to save the whole list
        as well could overwrite changes.  The safest way to append to a list is
        to perform a push operation.
    """
    def __init__(self, field, **kwargs) -> None:
        ...
    
    def to_mongo(self, value, use_db_field=..., fields=...): # -> list[int | Any]:
        ...
    


def key_not_string(d): # -> Literal[True] | None:
    """Helper function to recursively determine if any key in a
    dictionary is not a string.
    """
    ...

def key_starts_with_dollar(d): # -> Literal[True] | None:
    """Helper function to recursively determine if any key in a
    dictionary starts with a dollar
    """
    ...

class DictField(ComplexBaseField):
    """A dictionary field that wraps a standard Python dictionary. This is
    similar to an embedded document, but the structure is not defined.

    .. note::
        Required means it cannot be empty - as the default for DictFields is {}
    """
    def __init__(self, field=..., *args, **kwargs) -> None:
        ...
    
    def validate(self, value): # -> None:
        """Make sure that a list of valid fields is being used."""
        ...
    
    def lookup_member(self, member_name): # -> DictField:
        ...
    
    def prepare_query_value(self, op, value): # -> Pattern[Any | str] | Pattern[Any] | dict[Any, Any] | str | list[Any] | dict[int | Any, Any]:
        ...
    


class MapField(DictField):
    """A field that maps a name to a specified field type. Similar to
    a DictField, except the 'value' of each item must match the specified
    field type.
    """
    def __init__(self, field=..., *args, **kwargs) -> None:
        ...
    


class ReferenceField(BaseField):
    """A reference to a document that will be automatically dereferenced on
    access (lazily).

    Note this means you will get a database I/O access everytime you access
    this field. This is necessary because the field returns a :class:`~mongoengine.Document`
    which precise type can depend of the value of the `_cls` field present in the
    document in database.
    In short, using this type of field can lead to poor performances (especially
    if you access this field only to retrieve it `pk` field which is already
    known before dereference). To solve this you should consider using the
    :class:`~mongoengine.fields.LazyReferenceField`.

    Use the `reverse_delete_rule` to handle what should happen if the document
    the field is referencing is deleted.  EmbeddedDocuments, DictFields and
    MapFields does not support reverse_delete_rule and an `InvalidDocumentError`
    will be raised if trying to set on one of these Document / Field types.

    The options are:

      * DO_NOTHING (0)  - don't do anything (default).
      * NULLIFY    (1)  - Updates the reference to null.
      * CASCADE    (2)  - Deletes the documents associated with the reference.
      * DENY       (3)  - Prevent the deletion of the reference object.
      * PULL       (4)  - Pull the reference from a :class:`~mongoengine.fields.ListField` of references

    Alternative syntax for registering delete rules (useful when implementing
    bi-directional delete rules)

    .. code-block:: python

        class Org(Document):
            owner = ReferenceField('User')

        class User(Document):
            org = ReferenceField('Org', reverse_delete_rule=CASCADE)

        User.register_delete_rule(Org, 'owner', DENY)
    """
    def __init__(self, document_type, dbref=..., reverse_delete_rule=..., **kwargs) -> None:
        """Initialises the Reference Field.

        :param document_type: The type of Document that will be referenced
        :param dbref:  Store the reference as :class:`~pymongo.dbref.DBRef`
          or as the :class:`~pymongo.objectid.ObjectId`.
        :param reverse_delete_rule: Determines what to do when the referring
          object is deleted
        :param kwargs: Keyword arguments passed into the parent :class:`~mongoengine.BaseField`

        .. note ::
            A reference to an abstract document type is always stored as a
            :class:`~pymongo.dbref.DBRef`, regardless of the value of `dbref`.
        """
        ...
    
    @property
    def document_type(self): # -> Any | type[Any] | type[Document] | None:
        ...
    
    def __get__(self, instance, owner): # -> Self:
        """Descriptor to allow lazy dereferencing."""
        ...
    
    def to_mongo(self, document): # -> Any | DBRef:
        ...
    
    def to_python(self, value): # -> DBRef | Document | EmbeddedDocument:
        """Convert a MongoDB-compatible type to a Python type."""
        ...
    
    def prepare_query_value(self, op, value): # -> Any | DBRef | None:
        ...
    
    def validate(self, value): # -> None:
        ...
    
    def lookup_member(self, member_name): # -> Any:
        ...
    


class CachedReferenceField(BaseField):
    """A referencefield with cache fields to purpose pseudo-joins"""
    def __init__(self, document_type, fields=..., auto_sync=..., **kwargs) -> None:
        """Initialises the Cached Reference Field.

        :param document_type: The type of Document that will be referenced
        :param fields:  A list of fields to be cached in document
        :param auto_sync: if True documents are auto updated
        :param kwargs: Keyword arguments passed into the parent :class:`~mongoengine.BaseField`
        """
        ...
    
    def start_listener(self): # -> None:
        ...
    
    def on_document_pre_save(self, sender, document, created, **kwargs): # -> None:
        ...
    
    def to_python(self, value): # -> Self | Any:
        ...
    
    @property
    def document_type(self): # -> Any | type[Any] | type[Document] | None:
        ...
    
    def __get__(self, instance, owner): # -> Self:
        ...
    
    def to_mongo(self, document, use_db_field=..., fields=...): # -> SON[str, Any]:
        ...
    
    def prepare_query_value(self, op, value): # -> dict[str, Any | None] | None:
        ...
    
    def validate(self, value): # -> None:
        ...
    
    def lookup_member(self, member_name): # -> Any:
        ...
    
    def sync_all(self): # -> None:
        """
        Sync all cached fields on demand.
        Caution: this operation may be slower.
        """
        ...
    


class GenericReferenceField(BaseField):
    """A reference to *any* :class:`~mongoengine.document.Document` subclass
    that will be automatically dereferenced on access (lazily).

    Note this field works the same way as :class:`~mongoengine.document.ReferenceField`,
    doing database I/O access the first time it is accessed (even if it's to access
    it ``pk`` or ``id`` field).
    To solve this you should consider using the
    :class:`~mongoengine.fields.GenericLazyReferenceField`.

    .. note ::
        * Any documents used as a generic reference must be registered in the
          document registry.  Importing the model will automatically register
          it.

        * You can use the choices param to limit the acceptable Document types
    """
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def __get__(self, instance, owner): # -> Self:
        ...
    
    def validate(self, value): # -> None:
        ...
    
    def to_mongo(self, document): # -> dict[Any, Any] | SON[Any, Any] | ObjectId | DBRef | SON[str, DBRef] | None:
        ...
    
    def prepare_query_value(self, op, value): # -> dict[Any, Any] | SON[Any, Any] | ObjectId | DBRef | SON[str, DBRef] | None:
        ...
    


class BinaryField(BaseField):
    """A binary data field."""
    def __init__(self, max_bytes=..., **kwargs) -> None:
        ...
    
    def __set__(self, instance, value): # -> None:
        """Handle bytearrays in python 3.1"""
        ...
    
    def to_mongo(self, value): # -> Binary:
        ...
    
    def validate(self, value): # -> None:
        ...
    
    def prepare_query_value(self, op, value): # -> Binary:
        ...
    


class EnumField(BaseField):
    """Enumeration Field. Values are stored underneath as is,
    so it will only work with simple types (str, int, etc) that
    are bson encodable

    Example usage:

    .. code-block:: python

        class Status(Enum):
            NEW = 'new'
            ONGOING = 'ongoing'
            DONE = 'done'

        class ModelWithEnum(Document):
            status = EnumField(Status, default=Status.NEW)

        ModelWithEnum(status='done')
        ModelWithEnum(status=Status.DONE)

    Enum fields can be searched using enum or its value:

    .. code-block:: python

        ModelWithEnum.objects(status='new').count()
        ModelWithEnum.objects(status=Status.NEW).count()

    The values can be restricted to a subset of the enum by using the ``choices`` parameter:

    .. code-block:: python

        class ModelWithEnum(Document):
            status = EnumField(Status, choices=[Status.NEW, Status.DONE])
    """
    def __init__(self, enum, **kwargs) -> None:
        ...
    
    def validate(self, value): # -> None:
        ...
    
    def to_python(self, value):
        ...
    
    def __set__(self, instance, value): # -> None:
        ...
    
    def to_mongo(self, value):
        ...
    
    def prepare_query_value(self, op, value):
        ...
    


class GridFSError(Exception):
    ...


class GridFSProxy:
    """Proxy object to handle writing and reading of files to and from GridFS"""
    _fs = ...
    def __init__(self, grid_id=..., key=..., instance=..., db_alias=..., collection_name=...) -> None:
        ...
    
    def __getattr__(self, name): # -> Any:
        ...
    
    def __get__(self, instance, value): # -> Self:
        ...
    
    def __bool__(self): # -> bool:
        ...
    
    def __getstate__(self): # -> dict[str, Any]:
        ...
    
    def __copy__(self): # -> GridFSProxy:
        ...
    
    def __deepcopy__(self, memo): # -> GridFSProxy:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    @property
    def fs(self): # -> GridFS:
        ...
    
    def get(self, grid_id=...): # -> GridOut | None:
        ...
    
    def new_file(self, **kwargs): # -> None:
        ...
    
    def put(self, file_obj, **kwargs): # -> None:
        ...
    
    def write(self, string): # -> None:
        ...
    
    def writelines(self, lines): # -> None:
        ...
    
    def read(self, size=...): # -> bytes | Literal[''] | None:
        ...
    
    def delete(self): # -> None:
        ...
    
    def replace(self, file_obj, **kwargs): # -> None:
        ...
    
    def close(self): # -> None:
        ...
    


class FileField(BaseField):
    """A GridFS storage field."""
    proxy_class = GridFSProxy
    def __init__(self, db_alias=..., collection_name=..., **kwargs) -> None:
        ...
    
    def __get__(self, instance, owner): # -> Self | proxy_class:
        ...
    
    def __set__(self, instance, value): # -> None:
        ...
    
    def get_proxy_obj(self, key, instance, db_alias=..., collection_name=...): # -> proxy_class:
        ...
    
    def to_mongo(self, value): # -> Any | None:
        ...
    
    def to_python(self, value): # -> proxy_class | None:
        ...
    
    def validate(self, value): # -> None:
        ...
    


class ImageGridFsProxy(GridFSProxy):
    """Proxy for ImageField"""
    def put(self, file_obj, **kwargs): # -> None:
        """
        Insert a image in database
        applying field properties (size, thumbnail_size)
        """
        ...
    
    def delete(self, *args, **kwargs): # -> None:
        ...
    
    @property
    def size(self): # -> tuple[Any, Any] | None:
        """
        return a width, height of image
        """
        ...
    
    @property
    def format(self): # -> Any | None:
        """
        return format of image
        ex: PNG, JPEG, GIF, etc
        """
        ...
    
    @property
    def thumbnail(self): # -> GridOut | None:
        """
        return a gridfs.grid_file.GridOut
        representing a thumbnail of Image
        """
        ...
    
    def write(self, *args, **kwargs):
        ...
    
    def writelines(self, *args, **kwargs):
        ...
    


class ImproperlyConfigured(Exception):
    ...


class ImageField(FileField):
    """
    A Image File storage field.

    :param size: max size to store images, provided as (width, height, force)
        if larger, it will be automatically resized (ex: size=(800, 600, True))
    :param thumbnail_size: size to generate a thumbnail, provided as (width, height, force)
    """
    proxy_class = ImageGridFsProxy
    def __init__(self, size=..., thumbnail_size=..., collection_name=..., **kwargs) -> None:
        ...
    


class SequenceField(BaseField):
    """Provides a sequential counter see:
     https://www.mongodb.com/docs/manual/reference/method/ObjectId/#ObjectIDs-SequenceNumbers

    .. note::

             Although traditional databases often use increasing sequence
             numbers for primary keys. In MongoDB, the preferred approach is to
             use Object IDs instead.  The concept is that in a very large
             cluster of machines, it is easier to create an object ID than have
             global, uniformly increasing sequence numbers.

    :param collection_name:  Name of the counter collection (default 'mongoengine.counters')
    :param sequence_name: Name of the sequence in the collection (default 'ClassName.counter')
    :param value_decorator: Any callable to use as a counter (default int)

    Use any callable as `value_decorator` to transform calculated counter into
    any value suitable for your needs, e.g. string or hexadecimal
    representation of the default integer counter value.

    .. note::

        In case the counter is defined in the abstract document, it will be
        common to all inherited documents and the default sequence name will
        be the class name of the abstract document.
    """
    _auto_gen = ...
    COLLECTION_NAME = ...
    VALUE_DECORATOR = int
    def __init__(self, collection_name=..., db_alias=..., sequence_name=..., value_decorator=..., *args, **kwargs) -> None:
        ...
    
    def generate(self): # -> int:
        """
        Generate and Increment the counter
        """
        ...
    
    def set_next_value(self, value): # -> int:
        """Helper method to set the next sequence value"""
        ...
    
    def get_next_value(self): # -> int:
        """Helper method to get the next value for previewing.

        .. warning:: There is no guarantee this will be the next value
        as it is only fixed on set.
        """
        ...
    
    def get_sequence_name(self): # -> LiteralString:
        ...
    
    def __get__(self, instance, owner): # -> int | Self:
        ...
    
    def __set__(self, instance, value): # -> None:
        ...
    
    def prepare_query_value(self, op, value): # -> int:
        """
        This method is overridden in order to convert the query value into to required
        type. We need to do this in order to be able to successfully compare query
        values passed as string, the base implementation returns the value as is.
        """
        ...
    
    def to_python(self, value): # -> int:
        ...
    


class UUIDField(BaseField):
    """A UUID field."""
    _binary = ...
    def __init__(self, binary=..., **kwargs) -> None:
        """
        Store UUID data in the database

        :param binary: if False store as a string.
        """
        ...
    
    def to_python(self, value): # -> UUID:
        ...
    
    def to_mongo(self, value): # -> str | UUID:
        ...
    
    def prepare_query_value(self, op, value): # -> str | UUID | None:
        ...
    
    def validate(self, value): # -> None:
        ...
    


class GeoPointField(BaseField):
    """A list storing a longitude and latitude coordinate.

    .. note:: this represents a generic point in a 2D plane and a legacy way of
        representing a geo point. It admits 2d indexes but not "2dsphere" indexes
        in MongoDB > 2.4 which are more natural for modeling geospatial points.
        See :ref:`geospatial-indexes`
    """
    _geo_index = ...
    def validate(self, value): # -> None:
        """Make sure that a geo-value is of type (x, y)"""
        ...
    


class PointField(GeoJsonBaseField):
    """A GeoJSON field storing a longitude and latitude coordinate.

    The data is represented as:

    .. code-block:: js

        {'type' : 'Point' ,
         'coordinates' : [x, y]}

    You can either pass a dict with the full information or a list
    to set the value.

    Requires mongodb >= 2.4
    """
    _type = ...


class LineStringField(GeoJsonBaseField):
    """A GeoJSON field storing a line of longitude and latitude coordinates.

    The data is represented as:

    .. code-block:: js

        {'type' : 'LineString' ,
         'coordinates' : [[x1, y1], [x2, y2] ... [xn, yn]]}

    You can either pass a dict with the full information or a list of points.

    Requires mongodb >= 2.4
    """
    _type = ...


class PolygonField(GeoJsonBaseField):
    """A GeoJSON field storing a polygon of longitude and latitude coordinates.

    The data is represented as:

    .. code-block:: js

        {'type' : 'Polygon' ,
         'coordinates' : [[[x1, y1], [x1, y1] ... [xn, yn]],
                          [[x1, y1], [x1, y1] ... [xn, yn]]}

    You can either pass a dict with the full information or a list
    of LineStrings. The first LineString being the outside and the rest being
    holes.

    Requires mongodb >= 2.4
    """
    _type = ...


class MultiPointField(GeoJsonBaseField):
    """A GeoJSON field storing a list of Points.

    The data is represented as:

    .. code-block:: js

        {'type' : 'MultiPoint' ,
         'coordinates' : [[x1, y1], [x2, y2]]}

    You can either pass a dict with the full information or a list
    to set the value.

    Requires mongodb >= 2.6
    """
    _type = ...


class MultiLineStringField(GeoJsonBaseField):
    """A GeoJSON field storing a list of LineStrings.

    The data is represented as:

    .. code-block:: js

        {'type' : 'MultiLineString' ,
         'coordinates' : [[[x1, y1], [x1, y1] ... [xn, yn]],
                          [[x1, y1], [x1, y1] ... [xn, yn]]]}

    You can either pass a dict with the full information or a list of points.

    Requires mongodb >= 2.6
    """
    _type = ...


class MultiPolygonField(GeoJsonBaseField):
    """A GeoJSON field storing  list of Polygons.

    The data is represented as:

    .. code-block:: js

        {'type' : 'MultiPolygon' ,
         'coordinates' : [[
               [[x1, y1], [x1, y1] ... [xn, yn]],
               [[x1, y1], [x1, y1] ... [xn, yn]]
           ], [
               [[x1, y1], [x1, y1] ... [xn, yn]],
               [[x1, y1], [x1, y1] ... [xn, yn]]
           ]
        }

    You can either pass a dict with the full information or a list
    of Polygons.

    Requires mongodb >= 2.6
    """
    _type = ...


class LazyReferenceField(BaseField):
    """A really lazy reference to a document.
    Unlike the :class:`~mongoengine.fields.ReferenceField` it will
    **not** be automatically (lazily) dereferenced on access.
    Instead, access will return a :class:`~mongoengine.base.LazyReference` class
    instance, allowing access to `pk` or manual dereference by using
    ``fetch()`` method.
    """
    def __init__(self, document_type, passthrough=..., dbref=..., reverse_delete_rule=..., **kwargs) -> None:
        """Initialises the Reference Field.

        :param dbref:  Store the reference as :class:`~pymongo.dbref.DBRef`
          or as the :class:`~pymongo.objectid.ObjectId`.id .
        :param reverse_delete_rule: Determines what to do when the referring
          object is deleted
        :param passthrough: When trying to access unknown fields, the
          :class:`~mongoengine.base.datastructure.LazyReference` instance will
          automatically call `fetch()` and try to retrieve the field on the fetched
          document. Note this only work getting field (not setting or deleting).
        """
        ...
    
    @property
    def document_type(self): # -> Any | type[Document] | None:
        ...
    
    def build_lazyref(self, value): # -> LazyReference:
        ...
    
    def __get__(self, instance, owner): # -> Self:
        """Descriptor to allow lazy dereferencing."""
        ...
    
    def to_mongo(self, value): # -> DBRef:
        ...
    
    def to_python(self, value): # -> LazyReference | DBRef | Document | EmbeddedDocument:
        """Convert a MongoDB-compatible type to a Python type."""
        ...
    
    def validate(self, value): # -> None:
        ...
    
    def prepare_query_value(self, op, value): # -> DBRef | None:
        ...
    
    def lookup_member(self, member_name):
        ...
    


class GenericLazyReferenceField(GenericReferenceField):
    """A reference to *any* :class:`~mongoengine.document.Document` subclass.
    Unlike the :class:`~mongoengine.fields.GenericReferenceField` it will
    **not** be automatically (lazily) dereferenced on access.
    Instead, access will return a :class:`~mongoengine.base.LazyReference` class
    instance, allowing access to `pk` or manual dereference by using
    ``fetch()`` method.

    .. note ::
        * Any documents used as a generic reference must be registered in the
          document registry.  Importing the model will automatically register
          it.

        * You can use the choices param to limit the acceptable Document types
    """
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def build_lazyref(self, value): # -> LazyReference:
        ...
    
    def __get__(self, instance, owner): # -> Self:
        ...
    
    def validate(self, value): # -> None:
        ...
    
    def to_mongo(self, document): # -> SON[str, DBRef] | dict[Any, Any] | SON[Any, Any] | ObjectId | DBRef | None:
        ...
    


class Decimal128Field(BaseField):
    """
    128-bit decimal-based floating-point field capable of emulating decimal
    rounding with exact precision. This field will expose decimal.Decimal but stores the value as a
    `bson.Decimal128` behind the scene, this field is intended for monetary data, scientific computations, etc.
    """
    DECIMAL_CONTEXT = ...
    def __init__(self, min_value=..., max_value=..., **kwargs) -> None:
        ...
    
    def to_mongo(self, value): # -> Decimal128 | None:
        ...
    
    def to_python(self, value): # -> Decimal | None:
        ...
    
    def validate(self, value): # -> None:
        ...
    
    def prepare_query_value(self, op, value): # -> Decimal128 | None:
        ...
    


