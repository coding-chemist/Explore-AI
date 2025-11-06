"""Core helpers and configuration exports.

Expose `config` and `models` at package level so callers can do either
`from core.config import app` or `from app.core.config import app`.
"""
from . import config
from . import models

__all__ = ["config", "models"]
