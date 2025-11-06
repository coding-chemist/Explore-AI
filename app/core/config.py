from typing import Dict
from typing import List
from typing import Optional

from pydantic import Field

from .models import AppInfo
from .models import BaseModel
from .models import Page
from .models import Paths
from .models import Theme


# Page metadata: keep routing / colors centralized so other modules can
# import typed page information instead of duplicating heuristics.
class PageMeta(BaseModel):
    page: Page
    color: str
    keywords: List[str] = Field(default_factory=list)
    module: Optional[str] = None


page_meta: Dict[Page, PageMeta] = {
    Page.ml: PageMeta(
        page=Page.ml,
        color="#f7308c",
        keywords=["machine", "ml"],
        module="pages.ml",
    ),
    Page.dl: PageMeta(
        page=Page.dl,
        color="#ccff00",
        keywords=["deep", "dl"],
        module="pages.dl",
    ),
    Page.genai: PageMeta(
        page=Page.genai,
        color="#ffeb3b",
        keywords=["gen", "generative"],
        module="pages.genai",
    ),
    Page.agenticai: PageMeta(
        page=Page.agenticai,
        color="#00d9ff",
        keywords=["agent"],
        module="pages.agenticai",
    ),
    Page.home: PageMeta(
        page=Page.home,
        color="var(--c-cyan)",
        keywords=["home"],
        module="Home",
    ),
    Page.landing: PageMeta(
        page=Page.landing,
        color="var(--c-cyan)",
        keywords=["landing"],
        module="Landing",
    ),
}


# Export ready-to-use instances (Pydantic BaseModel instances).
# Other modules should import these (typed) singletons.
paths = Paths()
theme = Theme()
app = AppInfo()
