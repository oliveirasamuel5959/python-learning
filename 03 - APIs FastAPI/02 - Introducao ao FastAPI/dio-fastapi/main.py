from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI()

fake_db = [
  {'title': f'FastAPI Basics com Django', 'date': datetime.now(timezone.utc), 'published': True},
  {'title': f'um app com Fastapi', 'date': datetime.now(timezone.utc), 'published': True},
  {'title': f'FastAPI Basics com Flask', 'date': datetime.now(timezone.utc), 'published': True},
  {'title': f'um app com Starlette', 'date': datetime.now(timezone.utc), 'published': False},
]


@app.get("/posts")
def read_posts(skip: int = 0, limit: int = len(fake_db), published: bool = True):
    return [post for post in fake_db[skip : skip + limit] if post['published'] is published]


@app.get("/posts/{framework}")
def read_framework_posts(framework: int):
    return {"posts": [
      {'title': f'FastAPI Basics com {framework}', 'date': datetime.now(timezone.utc)},
      {'title': f'um app com {framework}', 'date': datetime.now(timezone.utc)},
      {'content': 'Learn how to build APIs with FastAPI!'}
    ]
  }