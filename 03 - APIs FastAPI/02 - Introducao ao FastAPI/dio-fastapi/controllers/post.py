from fastapi import status, Cookie, Response, Header, APIRouter
from typing import Annotated

from datetime import datetime, timezone
from schemas.post import PostIn
from views.post import PostOut

router = APIRouter(prefix="/posts")

fake_db = [
    {
        "title": f"FastAPI Basics com Django",
        "date": datetime.now(timezone.utc),
        "published": True,
    },
    {
        "title": f"um app com Fastapi",
        "date": datetime.now(timezone.utc),
        "published": True,
    },
    {
        "title": f"FastAPI Basics com Flask",
        "date": datetime.now(timezone.utc),
        "published": True,
    },
    {
        "title": f"um app com Starlette",
        "date": datetime.now(timezone.utc),
        "published": False,
    },
]


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn):
    fake_db.append(post.model_dump())
    return post


@router.get("/", response_model=list[PostOut])
def read_posts(
    published: bool,
    skip: int = 0,
    limit: int = len(fake_db),
    ads_id: Annotated[str | None, Cookie()] = None,
):
    print(f"Cookie: {ads_id}")
    posts = []
    for post in fake_db:
        if len(posts) >= limit:
            break
        if post["published"] is published:
            posts.append(post)
    return posts


@router.get("/{framework}", response_model=PostOut)
def read_framework_posts(framework: int):
    return {
        "posts": [
            {
                "title": f"FastAPI Basics com {framework}",
                "date": datetime.now(timezone.utc),
            },
            {"title": f"um app com {framework}", "date": datetime.now(timezone.utc)},
            {"content": "Learn how to build APIs with FastAPI!"},
        ]
    }