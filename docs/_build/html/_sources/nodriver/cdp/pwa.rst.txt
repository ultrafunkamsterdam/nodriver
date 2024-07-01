PWA
===

This domain allows interacting with the browser to control PWAs.

*This CDP domain is experimental.*

.. module:: nodriver.cdp.pwa

* Types_
* Commands_
* Events_

Types
-----

Generally, you do not need to instantiate CDP types
yourself. Instead, the API creates objects for you as return
values from commands, and then you can use those objects as
arguments to other commands.

.. autoclass:: FileHandlerAccept
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: FileHandler
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

.. autoclass:: DisplayMode
      :members:
      :undoc-members:
      :exclude-members: from_json, to_json

Commands
--------

Each command is a generator function. The return
type ``Generator[x, y, z]`` indicates that the generator
*yields* arguments of type ``x``, it must be resumed with
an argument of type ``y``, and it returns type ``z``. In
this library, types ``x`` and ``y`` are the same for all
commands, and ``z`` is the return type you should pay attention
to. For more information, see
:ref:`Getting Started: Commands <getting-started-commands>`.

.. autofunction:: change_app_user_settings

.. autofunction:: get_os_app_state

.. autofunction:: install

.. autofunction:: launch

.. autofunction:: launch_files_in_app

.. autofunction:: open_current_page_in_app

.. autofunction:: uninstall

Events
------

*There are no events in this module.*
