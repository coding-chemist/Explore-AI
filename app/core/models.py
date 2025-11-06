from enum import Enum
from pathlib import Path
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

# Central paths used by the app. Keep these defined here so other modules
# can import clean Pydantic models instead of re-defining defaults.
ROOT = Path(__file__).resolve().parents[2]
TEMPLATES_DIR = Path(__file__).resolve().parents[1] / "templates"


class Paths(BaseModel):
    root: Path = Field(default_factory=lambda: ROOT)
    assets: Path = Field(default_factory=lambda: ROOT / "assets")
    styles: Path = Field(default_factory=lambda: ROOT / "styles")
    templates: Path = Field(default_factory=lambda: TEMPLATES_DIR)


class Theme(BaseModel):
    black: str = "#000000"
    gray_900: str = "#111111"
    cyan: str = "#00F5FF"
    electric: str = "#00D9FF"
    violet: str = "#7B2FF7"
    text_primary: str = "#F5F7FA"
    text_muted: str = "#A3A3A3"
    gradient_primary: str = (
        "linear-gradient(90deg, #00F5FF, #00D9FF 35%, #7B2FF7 75%)"
    )


class AppInfo(BaseModel):
    app_name: str = "Explore‑AI"
    tagline: str = (
        "A Place for Mastering AI — from Classic ML to Modern Generative "
        "and Agentic AI."
    )
    logo_file: str = "logo.svg"
    hero_gif: str = "gifs/ai_hero.gif"
    page_icon: str = "🧠"


class UIMessage(BaseModel):
    title: str
    message: str | None = None
    back_href: str = "?page=home"
    back_label: str = "Back to Topics"
    # Optional explicit page hint (prefer passing this when available)
    page: Optional["Page"] = None


class Page(str, Enum):
    """Allowed page identifiers used by the app routing.

    Using a `str`-backed Enum makes it easy to coerce and compare values
    received from query parameters while keeping type-safety.
    """

    landing = "landing"
    home = "home"
    ml = "ml"
    genai = "genai"
    agenticai = "agenticai"
    dl = "dl"
