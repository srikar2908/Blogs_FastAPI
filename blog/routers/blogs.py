from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import blog
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

get_db = database.get_db

@router.get("/",response_model=List[schemas.ShowBlog])
def get_all(db: Session= Depends(database.get_db),current_user: schemas.User=Depends(blog.get_current_user)):
    return blog.get_all(db)



@router.post("/",status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User=Depends(get_current_user)):
    return blog.create(request, db)

# @app.get("/blog",response_model=List[schemas.ShowBlog], tags=["Blogs"])
# def get_all(db: Session= Depends(get_db)):
#     blogs=db.query(models.Blog).all()
#     return blogs

@router.get("/{id}", response_model=schemas.ShowBlog)
def get_blog(id:int,response:Response, db: Session= Depends(get_db),current_user: schemas.User=Depends(get_current_user)):
    return blog.get_blog(id, response, db)

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int, db:Session=Depends(get_db),current_user: schemas.User=Depends(get_current_user)):
    return blog.delete_blog(id, db)


@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int,request:schemas.Blog, db:Session=Depends(get_db),current_user: schemas.User=Depends(get_current_user)):
    return blog.update_blog(id, request, db)

