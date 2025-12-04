from fastapi import FastAPI ,Depends, HTTPException, status
from typing import List
from blog import schemas, models
from blog.database import engine, get_db
from sqlalchemy.orm import Session 
from .routers import blog, user, authentication

from passlib.context import CryptContext

app=FastAPI()
models.Base.metadata.create_all(engine)
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


# from pydantic import BaseModel
# app=FastAPI()
# class blog(BaseModel):
#     title:str
#     name:str
# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
# @app.post('/blog',status_code=201)
# def create(request: schemas.Blog,db:Session=Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog
# @app.get("/blogs")
# def get_all_blogs(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs
@app.get("/blog/{id}")
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog
@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found"
        )

    db.delete(blog)
    db.commit()
    return
# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
# def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)

#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with id {id} not found")

#     blog.update(request)
#     db.commit()

#     return 'updated'
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request:schemas.Blog, db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status. HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    blog.update(request.dict())
    db.commit()
    return 'updated'

#create user code
# pwd_cxt = CryptContext(schemes=['bcrypt'],deprecated='auto')
# @app.post('/user',response_model=schemas.ShowUser)
# def create_user(request:schemas.User,db:Session=Depends(get_db)):
#     hashedPassword = pwd_cxt.hash(request.password)
#     new_user = models.User(name=request.name, email=request.email, password=hashedPassword)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user
