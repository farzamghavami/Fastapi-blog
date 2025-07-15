from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from schemas import users as schemas
from models import users as models
from dependencies import get_db

router = APIRouter()

@router.post('/users/create/', response_model=schemas.User)
def create_user(user:schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email==user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail= 'email already exists')
    new_user = models.User(email=user.email, username=user.username, password= user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/users/{user_id}', response_model=schemas.User)
def get_user(user_id:int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id==user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user