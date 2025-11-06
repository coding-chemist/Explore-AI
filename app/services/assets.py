import base64
from pathlib import Path

from core.config import app
from core.config import paths


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_css(*files: str) -> str:
    parts = []
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


def gif_src() -> str:
    local = paths.assets / app.hero_gif
    if local.exists():
        # return a base64 data URI so the GIF can be embedded inline
        data = base64.b64encode(local.read_bytes()).decode("utf-8")
        # guess mime type by suffix
        suffix = local.suffix.lower()
        if suffix == ".gif":
            mime = "image/gif"
        elif suffix == ".png":
            mime = "image/png"
        elif suffix in (".jpg", ".jpeg"):
            mime = "image/jpeg"
        else:
            mime = "application/octet-stream"
        return f"data:{mime};base64,{data}"

    return "https://c.tenor.com/ow94qLGI8WsAAAAC/ai.gif"


def asset_data_uri(relpath: str) -> str:
    """Return a data URI for an asset located under the assets/ folder.

    If the file does not exist, return a 1x1 transparent PNG data URI as a
    harmless fallback.
    """
    local = paths.assets / relpath
    if local.exists():
        data = base64.b64encode(local.read_bytes()).decode("utf-8")
        suffix = local.suffix.lower()
        if suffix == ".png":
            mime = "image/png"
        elif suffix == ".jpg" or suffix == ".jpeg":
            mime = "image/jpeg"
        elif suffix == ".gif":
            mime = "image/gif"
        elif suffix == ".svg":
            mime = "image/svg+xml"
        else:
            mime = "application/octet-stream"
        return f"data:{mime};base64,{data}"

    # 1x1 transparent PNG
    return (
        "data:image/png;base64,"
        + "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAAMA"
        "ASsJTYQAAAAASUVORK5CYII="
    )
