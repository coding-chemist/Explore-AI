"""App package initializer.

This file sets up a couple of conveniences for running the app both as
"python -m app" / "streamlit run app/main.py" and for local imports used
throughout the codebase. Historically the repository contains imports like
"from core.config import ..." and "from services.assets import ..."; to keep
those working when the package is imported we expose the subpackages as
top-level aliases in sys.modules.

This is intentionally conservative and only creates module aliases; it does
not change runtime behavior beyond allowing both "app.core" and plain
"core" to resolve to the same package when this package is imported.
"""
import sys

from . import components
from . import core
from . import pages
from . import services

# Create top-level aliases so code that uses "from core.config import ..."
# continues to work when the package is imported as `app`.
sys.modules.setdefault("core", core)
sys.modules.setdefault("components", components)
sys.modules.setdefault("services", services)
sys.modules.setdefault("pages", pages)

__all__ = ["core", "components", "services", "pages"]
