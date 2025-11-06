from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings

ROOT = Path(__file__).resolve().parents[2]
TEMPLATES_DIR = Path(__file__).resolve().parents[1] / "templates"


class Paths(BaseSettings):
    root: Path = Field(default_factory=lambda: ROOT)
    assets: Path = Field(default_factory=lambda: ROOT / "assets")
    styles: Path = Field(default_factory=lambda: ROOT / "styles")
    templates: Path = Field(default_factory=lambda: TEMPLATES_DIR)


class ThemeConfig(BaseSettings):
    black: str = "#000000"
    gray_900: str = "#111111"
    cyan: str = "#00F5FF"
    electric: str = "#00D9FF"
    violet: str = "#7B2FF7"
    text_primary: str = "#F5F7FA"
    text_muted: str = "#A3A3A3"
    gradient_primary: str = "linear-gradient(90deg, #00F5FF, #00D9FF 35%, #7B2FF7 75%)"


class AppConfig(BaseSettings):
    app_name: str = "Explore‑AI"
    tagline: str = (
        "A Place for Mastering AI — from Classic ML to Modern Generative "
        "and Agentic AI."
    )
    logo_file: str = "logo.svg"
    hero_gif: str = "gifs/ai_hero.gif"
    page_icon: str = "🧠"


paths = Paths()
theme = ThemeConfig()
app = AppConfig()
