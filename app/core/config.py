from .models import AppInfo
from .models import Paths
from .models import Theme


# Export ready-to-use instances (Pydantic BaseModel instances).
# Other modules should import these (typed) singletons.
paths = Paths()
theme = Theme()
app = AppInfo()
