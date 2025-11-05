from pydantic import BaseModel
from pydantic import AwareDatetime
from pydantic import NaiveDatetime

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    published_at: AwareDatetime | NaiveDatetime | None
