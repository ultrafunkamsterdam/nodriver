# Other classes and Helper classes

## Config class

### *class* Config(user_data_dir=None, headless=False, browser_executable_path=None, browser_args=None, sandbox=True, lang='en-US,en;q=0.9', \*\*kwargs)

#### add_argument(arg)

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

## ContraDict class

Many components in this package are built using a
base class of [`nodriver.core._contradict.ContraDict`](#nodriver.core._contradict.ContraDict).

It’s nothing more than a dictionary which has attribute access AND
is JSON serializable.

### *class* ContraDict(\*args, \*\*kwargs)

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
