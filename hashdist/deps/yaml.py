# when this module loads, it redirects all future
# lookups to the appropriate yaml implementation

import sys

from .six import PY2, PY3

if PY2:
    from . import yaml2 as yaml
elif PY3:
    from . import yaml3 as yaml
else:
    raise RuntimeError("unknown version of python running")

sys.modules[__name__] = yaml
