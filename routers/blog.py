from fastapi import APIRouter, Depends, status
from .. import schemas, database, models,oaut2
from sqlalchemy.orm import Session
from ..repository import blog


router=APIRouter(
    prefix='/blog',
)
@router.get("/")
def get_all_blogs(db: Session = Depends(database.get_db),get_current_user:schemas.User=Depends(oaut2.get_current_user)):
    # blogs = db.query(models.Blog).all()
    # return blogs
    return blog.get_all(db)
@router.post('/',status_code=201)
def create(request: schemas.Blog,db:Session=Depends(database.get_db)):
    # new_blog = models.Blog(title=request.title, body=request.body)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog
    return blog.create_all(request, db)
