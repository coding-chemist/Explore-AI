import base64
import mimetypes
from enum import Enum
from pathlib import Path

from core.config import app
from core.config import paths
from pydantic import BaseModel


# ---------------------------------------------------------------------
# ENUM: known suffixes
# ---------------------------------------------------------------------
class Suffix(str, Enum):
    PNG = ".png"
    JPG = ".jpg"
    JPEG = ".jpeg"
    GIF = ".gif"
    SVG = ".svg"
    OTHER = ""


# ---------------------------------------------------------------------
# MIME map builder (dynamic)
# ---------------------------------------------------------------------
def _build_mime_map() -> dict[str, str]:
    """
    Build a dynamic extension → MIME mapping.

    Uses Python's built-in mimetypes table (which includes OS mime.types)
    and fills in any common gaps such as SVG.
    """
    mimetypes.init()
    mimetypes.add_type("image/svg+xml", ".svg")  # some OS tables miss this

    mime_map: dict[str, str] = {}
    for ext in Suffix:
        if not ext.value:
            continue
        mt, _ = mimetypes.guess_type(f"file{ext.value}")
        mime_map[ext.value] = mt or "application/octet-stream"
    return mime_map


# global map built once at import
MIME_MAP = _build_mime_map()


def register_mime(ext: str, mime: str) -> None:
    """Register or override a MIME type for an extension at runtime."""
    if not ext.startswith("."):
        ext = f".{ext}"
    MIME_MAP[ext.lower()] = mime


# ---------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------
def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_css(*files: str) -> str:
    parts: list[str] = []
    for f in files:
        p = paths.styles / f
        if p.exists():
            parts.append(read_text(p))
    return "\n\n".join(parts)


def load_template(rel: str) -> str:
    return read_text(paths.templates / rel)


def load_logo_base64() -> str:
    logo_path = paths.assets / app.logo_file
    encoded = base64.b64encode(logo_path.read_bytes()).decode("utf-8")
    if logo_path.suffix.lower() == ".svg":
        return f"data:image/svg+xml;base64,{encoded}"
    return f"data:image/png;base64,{encoded}"


# ---------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------
class SuffixModel(BaseModel):
    """Represent and normalize a file suffix and provide a MIME type."""

    suffix: str

    @property
    def normalized(self) -> str:
        s = (self.suffix or "").lower()
        if s.startswith("."):
            return s
        for ext in Suffix:
            if not ext.value:
                continue
            if s.endswith(ext.value):
                return ext.value
        return ""

    @property
    def mime(self) -> str:
        s = self.normalized
        if s in MIME_MAP:
            return MIME_MAP[s]
        mt, _ = mimetypes.guess_type(f"file{s}")
        return mt or "application/octet-stream"


class AssetData(BaseModel):
    """Represent an asset on disk and produce a data URI."""

    path: Path
    b64: str
    mime: str

    @classmethod
    def from_path(cls, path: Path) -> "AssetData":
        data = base64.b64encode(path.read_bytes()).decode("utf-8")
        mime = SuffixModel(suffix=path.suffix).mime
        return cls(path=path, b64=data, mime=mime)

    def data_uri(self) -> str:
        return f"data:{self.mime};base64,{self.b64}"


# ---------------------------------------------------------------------
# Helpers for assets
# ---------------------------------------------------------------------
def gif_src() -> str:
    local = paths.assets / app.hero_gif
    if local.exists():
        return AssetData.from_path(local).data_uri()
    return "https://c.tenor.com/ow94qLGI8WsAAAAC/ai.gif"


def asset_data_uri(relpath: str) -> str:
    """Return a data URI for an asset located under assets/."""
    local = paths.assets / relpath
    if local.exists():
        return AssetData.from_path(local).data_uri()

    # 1×1 transparent PNG fallback
    return (
        "data:image/png;base64,"
        + "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAA"
        + "MAASsJTYQAAAAASUVORK5CYII="
    )
