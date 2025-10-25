from pydantic import BaseModel
from datetime import datetime, timezone

class PostOut(BaseModel):
    title: str
    date: datetime = datetime.now(timezone.utc)
    published: bool