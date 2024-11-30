from db import db, Base
from models import User, StudySet
from utils import hash_password

# Create all tables
Base.metadata.create_all(db.engine)


# service.py            --> controller/view


class UserService:

    # CRUD --> create/read/update/deletes

    def add_user(self, session, username, email, password, age):
        user = User(username=username, email=email, password=password, age=age)
        session.add(user)
        session.commit()
        return user
    
    def delete_user(session, user_id):        
        pass


user_service = UserService()

user_service.add_user(db.session, "yehor", "kirill@gmail.com", hash_password("q1w2e32323"), 22)         # HASHING PASSWORD
