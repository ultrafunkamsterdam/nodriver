import re
import warnings as _warnings
from collections.abc import Mapping as _Mapping, Sequence as _Sequence
import logging

__logger__ = logging.getLogger(__name__)


__all__ = ["cdict", "ContraDict"]


def cdict(*args, **kwargs):
    """
    factory function
    """
    return ContraDict(*args, **kwargs)


class ContraDict(dict):
    """
    directly inherited from dict

    accessible by attribute. o.x == o['x']
    This works also for all corner cases.

    native json.dumps and json.loads work with it

    names like "keys", "update", "values" etc won't overwrite the methods,
    but will just be available using dict lookup notation obj['items'] instead of obj.items

    all key names are converted to snake_case
    hyphen's (-), dot's (.) or whitespaces are replaced by underscore (_)

    autocomplete works even if the objects comes from a list

    recursive action. dict assignments will be converted too.
    """

    __module__ = None

    def __init__(self, *args, **kwargs):
        super().__init__()
        silent = False
        try:
            silent = kwargs.pop("silent")
        except:  # noqa
            pass
        _ = dict(*args, **kwargs)
        for key, val in _.copy().items():
            del _[key]
            key = _camel_to_snake(key)
            _[key] = val
        super().__setattr__("__dict__", self)
        for k, v in _.items():
            _check_key(k, self, False, silent)
            super().__setitem__(k, _wrap(self.__class__, v))

    def __setitem__(self, key, value):
        key = _camel_to_snake(key)
        super().__setitem__(key, _wrap(self.__class__, value))

    def __setattr__(self, key, value):
        key = _camel_to_snake(key)
        super().__setitem__(key, _wrap(self.__class__, value))

    def __getattribute__(self, attribute):
        attribute = _camel_to_snake(attribute)
        if not _check_key(attribute, self, boolean=True, silent=True):
            return getattr(super(), attribute)
        if attribute in self:
            return self[attribute]
        return object.__getattribute__(self, attribute)


def _wrap(cls, v):
    if isinstance(v, _Mapping):
        v = cls(v)

    elif isinstance(v, _Sequence) and not isinstance(
        v, (str, bytes, bytearray, set, tuple)
    ):
        v = list([_wrap(cls, x) for x in v])
    return v


_warning_names = (
    "items",
    "keys",
    "values",
    "update",
    "clear",
    "copy",
    "fromkeys",
    "get",
    "items",
    "keys",
    "pop",
    "popitem",
    "setdefault",
    "update",
    "values",
    "class",
)

_warning_names_message = """\n\
    While creating a ContraDict object, a key offending key name '{0}' has been found, which might behave unexpected.
    you will only be able to look it up using key, eg. myobject['{0}']. myobject.{0} will not work with that name.
    """


def _check_key(key: str, mapping: _Mapping, boolean: bool = False, silent=False):
    """checks `key` and warns if needed

    :param key:
    :param boolean: return True or False instead of passthrough
    :return:
    """
    e = None
    if not isinstance(key, (str,)):
        if boolean:
            return True
        return key
    if key.lower() in _warning_names or any(_ in key for _ in ("-", ".")):
        if not silent:
            __logger__.warning(_warning_names_message.format(key))
        e = True
    if not boolean:
        return key
    return not e


__RE_CAMEL_TO_SNAKE__ = re.compile("((?!^)(?<!_)[A-Z][a-z]+|(?<=[a-z0-9])[A-Z])")
__RE_SNAKE_TO_CAMEL__ = re.compile("(.*?)_([a-zA-Z])")


def _camel_to_snake(s):
    """
    Converts CamelCase/camelCase to snake_case
    :param str s: string to be converted
    :return: (str) snake_case version of s
    """
    s = s.replace("-", "").replace(".", "").replace(" ", "_")

    return __RE_CAMEL_TO_SNAKE__.sub(r"_\1", s).lower()


def _snake_to_camel(s):
    """
    Converts snake_case_string to camelCaseString
    :param str s: string to be converted
    :return: (str) camelCase version of s
    """
    return __RE_SNAKE_TO_CAMEL__.sub(lambda m: m.group(1) + m.group(2).upper(), s, 0)
