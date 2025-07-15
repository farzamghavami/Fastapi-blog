from pydantic import BaseModel
from typing import Optional, List

class CommentBase(BaseModel):
    content: str
    post_id: int
    parent_id: Optional[int] = None

class CommentCreate(CommentBase):
    pass

class CommentRead(CommentBase):
    id: int
    user_id: int
    replies: List['CommentRead'] = []

    class Config:
        orm_mode = True