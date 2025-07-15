from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import posts as post_models
from schemas import posts as post_schemas
from database import SessionLocal
from dependencies import get_db
from dependencies import get_current_user

router = APIRouter(prefix="/posts", tags=["posts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=post_schemas.PostRead)
def create_post(post: post_schemas.PostCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_post = post_models.Post(**post.dict(), owner_id=current_user.id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.get("/", response_model=list[post_schemas.PostRead])
def read_posts(db: Session = Depends(get_db)):
    return db.query(post_models.Post).all()

@router.get("/{post_id}", response_model=post_schemas.PostRead)
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(post_models.Post).filter(post_models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.put("/{post_id}", response_model=post_schemas.PostRead)
def update_post(post_id: int, post: post_schemas.PostUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_post = db.query(post_models.Post).filter(post_models.Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    if db_post.owner_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    db_post.title = post.title
    db_post.content = post.content
    db.commit()
    db.refresh(db_post)
    return db_post

@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_post = db.query(post_models.Post).filter(post_models.Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    if db_post.owner_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    db.delete(db_post)
    db.commit()
    return {"message": "Post deleted"}