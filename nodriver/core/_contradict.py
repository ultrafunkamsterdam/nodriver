import inspect
import warnings as _warnings
from collections.abc import Mapping as _Mapping, Sequence as _Sequence


class ContraDict(dict):
    """ """

    __module__ = None
    __hide_properties__ = False

    def __init__(self, *args, **kwargs):
        """
        ContraDict() -> new ContraDict initialized from a mapping object's
            (key, value) pairs
        ContraDict(iterable) -> new ContraDict initialized as if via:
            d = {}
            for k, v in iterable:
                d[k] = v
        ContraDict(**kwargs) -> new ContraDict initialized with the name=value pairs
            in the keyword argument list.  For example:  ContraDict(one=1, two=2)
        """
        super().__init__()
        silent = False
        try:
            silent = kwargs.pop("silent")
        except:  # noqa
            pass

        _ = dict(
            {
                k: v
                for k, v in self.__class__.__dict__.items()
                if (
                    type(k) is str
                    and not k.startswith("_")
                    and not callable(v)
                    and k not in self.__class__.__dict__
                )
            }
        )
        _.update(*args, **kwargs)

        super().__setattr__("__dict__", self)
        for k, v in _.items():
            _check_key(k, self, False, silent)
            super().__setitem__(k, _wrap(self.__class__, v))

    def __setitem__(self, key, value):
        super().__setitem__(key, _wrap(self.__class__, value))
        # self[key] = _wrap(self.__class__, value)

    def __setattr__(self, key, value):
        super().__setitem__(key, _wrap(self.__class__, value))

    def __getattribute__(self, attribute):
        if not _check_key(attribute, self, True, silent=True):
            # try:
            return getattr(super(), attribute)
            # except:
            #     raise
        return object.__getattribute__(self, attribute)

    def __dir__(self):
        a = list(self.keys())
        if self.__hide_properties__:
            a += [
                _ for _ in super().__dir__() if inspect.ismethod(getattr(self, _, None))
            ]
        return a


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
    ------------\n\
    this is just a warning. not an error\n\
    ------------\n\
    a key named '{0}' has been found, which might behave unexpected.\n
    it either matches a internal method name or contains hyphen(s) or period(s).\n
    you will only be able to look it up using key, eg. myobject['{0}'].
    myobject.{0} will not work with that name.
    \n
    offending name found in :\n
    {1}\n\n\
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
            _warnings.warn(_warning_names_message.format(key, {key: mapping}))
        e = True
    if not boolean:
        return key
    return not e
