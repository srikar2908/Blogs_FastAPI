from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..oauth2 import get_current_user


get_db = database.get_db

def get_all(db: Session= Depends(database.get_db),get_current_user: schemas.User=Depends(get_current_user)):
    blogs=db.query(models.Blog).all()
    return blogs



def create(request:schemas.Blog, db: Session = Depends(get_db)):
    new_blog=models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# @app.get("/blog",response_model=List[schemas.ShowBlog], tags=["Blogs"])
# def get_all(db: Session= Depends(get_db)):
#     blogs=db.query(models.Blog).all()
#     return blogs

def get_blog(id:int,response:Response, db: Session= Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=404,detail=f"Blog with id {id} is not available")

        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"detail": "Blog not found"}
    return blog


def delete_blog(id:int, db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=404,detail=f"Blog with id {id} is not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": f"Blog with id {id} has been deleted"}


def update_blog(id:int,request:schemas.Blog, db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=404,detail=f"Blog with id {id} is not available")
    blog.update({"title":request.title,"body":request.body})
    db.commit()
    return "updated successfully"


