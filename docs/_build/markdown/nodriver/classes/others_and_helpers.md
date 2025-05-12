# Other classes and Helper classes

## Config class

### *class* Config(user_data_dir=None, headless=False, browser_executable_path=None, browser_args=None, sandbox=True, lang='en-US', host=None, port=None, expert=None, \*\*kwargs)

Config object

#### *property* browser_args

#### *property* user_data_dir

#### *property* uses_custom_data_dir*: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### add_extension(extension_path)

adds an extension to load, you could point extension_path
to a folder (containing the manifest), or extension file (crx)

* **Parameters:**
  **extension_path** ([`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar)(`PathLike`, bound= [`str`](https://docs.python.org/3/library/stdtypes.html#str) | [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path))) – 
* **Returns:**
* **Return type:**

#### add_argument(arg)

## ContraDict class

Many components in this package are built using a
base class of [`nodriver.core._contradict.ContraDict`](#id0).

It’s nothing more than a dictionary which has attribute access AND
is JSON serializable.

### *class* ContraDict(\*args, \*\*kwargs)

directly inherited from dict

accessible by attribute. o.x == o[‘x’]
This works also for all corner cases.

native json.dumps and json.loads work with it

names like “keys”, “update”, “values” etc won’t overwrite the methods,
but will just be available using dict lookup notation obj[‘items’] instead of obj.items

all key names are converted to snake_case
hyphen’s (-), dot’s (.) or whitespaces are replaced by underscore (_)

autocomplete works even if the objects comes from a list

recursive action. dict assignments will be converted too.

#### clear()

#### copy()

#### fromkeys(value=None, /)

Create a new dictionary with keys from iterable and values set to value.

#### get(key, default=None, /)

Return the value for key if key is in the dictionary, else default.

#### items()

#### keys()

#### pop(k)

If the key is not found, return the default if given; otherwise,
raise a KeyError.

#### popitem()

Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order.
Raises KeyError if the dict is empty.

#### setdefault(key, default=None, /)

Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.

#### update(\*\*F)

If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
In either case, this is followed by: for k in F:  D[k] = F[k]

#### values()

## Helper functions

### cdict(\*args, \*\*kwargs)

factory function

### *class* ContraDict(\*args, \*\*kwargs)

directly inherited from dict

accessible by attribute. o.x == o[‘x’]
This works also for all corner cases.

native json.dumps and json.loads work with it

names like “keys”, “update”, “values” etc won’t overwrite the methods,
but will just be available using dict lookup notation obj[‘items’] instead of obj.items

all key names are converted to snake_case
hyphen’s (-), dot’s (.) or whitespaces are replaced by underscore (_)

autocomplete works even if the objects comes from a list

recursive action. dict assignments will be converted too.

#### clear()

#### copy()

#### fromkeys(value=None, /)

Create a new dictionary with keys from iterable and values set to value.

#### get(key, default=None, /)

Return the value for key if key is in the dictionary, else default.

#### items()

#### keys()

#### pop(k)

If the key is not found, return the default if given; otherwise,
raise a KeyError.

#### popitem()

Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order.
Raises KeyError if the dict is empty.

#### setdefault(key, default=None, /)

Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.

#### update(\*\*F)

If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
In either case, this is followed by: for k in F:  D[k] = F[k]

#### values()
