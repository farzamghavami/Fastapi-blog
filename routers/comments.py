from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import comments as comment_models
from schemas import comments as comment_schemas
from database import SessionLocal
from dependencies import get_db
from dependencies import get_current_user
from typing import List

router = APIRouter(prefix="/comments", tags=["comments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=comment_schemas.CommentRead)
def create_comment(comment: comment_schemas.CommentCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_comment = comment_models.Comment(**comment.dict(), user_id=current_user.id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

@router.get("/post/{post_id}", response_model=List[comment_schemas.CommentRead])
def get_comments_for_post(post_id: int, db: Session = Depends(get_db)):
    comments = db.query(comment_models.Comment).filter(comment_models.Comment.post_id == post_id, comment_models.Comment.parent_id == None).all()
    return comments

@router.get("/{comment_id}/replies", response_model=List[comment_schemas.CommentRead])
def get_replies(comment_id: int, db: Session = Depends(get_db)):
    replies = db.query(comment_models.Comment).filter(comment_models.Comment.parent_id == comment_id).all()
    return replies