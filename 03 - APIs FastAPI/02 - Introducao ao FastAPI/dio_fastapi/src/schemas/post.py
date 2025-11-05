from datetime import datetime, timezone
from pydantic import BaseModel

class PostIn(BaseModel):
    title: str
    content: str
    published_at: datetime | None = None
    published: bool = False