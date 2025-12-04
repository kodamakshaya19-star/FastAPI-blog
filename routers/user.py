from fastapi import APIRouter, Depends, status
from .. import schemas, database, models
from sqlalchemy.orm import Session
from passlib.context import CryptContext
router=APIRouter()
pwd_cxt = CryptContext(schemes=['bcrypt'],deprecated='auto')
@router.post('/user',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session=Depends(database.get_db)):
    hashedPassword = pwd_cxt.hash(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
