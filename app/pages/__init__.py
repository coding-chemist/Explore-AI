"""Pages package exports.

This exposes page modules so imports such as `from pages.ml import render`
work when the package is imported as `app`.
"""
from . import agenticai
from . import dl
from . import genai
from . import ml

__all__ = ["ml", "genai", "agenticai", "dl"]
