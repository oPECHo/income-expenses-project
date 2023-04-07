from ..core import models
from ..schemas import Scuser
from sqlalchemy.orm import Session
from ..utils.hashing import Hash

def create_user(request: Scuser.User, db: Session):
    new_user = models.User(username=request.username,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

