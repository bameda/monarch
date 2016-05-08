import os
import sys

try:
    from .local import *
    print("Loading local.py settings...", file=sys.stderr)
except ImportError:
    print("Loading development.py settings...", file=sys.stderr)
    from .development import *

