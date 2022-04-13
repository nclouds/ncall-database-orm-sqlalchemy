from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base


# connection engine
engine = create_engine(f"mysql://{env.MYSQL_USERNAME}:{env.MYSQL_PASSWORD}@{env.MYSQL_SERVER}/{env.MYSQL_DB}",echo = True)

# session
Session = sessionmaker(bind=engine)
new_session = Session()


# Base Class
Base = declarative_base()

# Users Model
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    address = Column(String(150))


# to create a table
# Base.metadata.create_all(engine)

# Insert data into users table
instance = Users(name="qaiser 1",address="xyz")
# to make changes in db we always need to add object to session and then commit the session
new_session.add(instance)
# to add array of objects we use session.add_all([instance1,instance2])
new_session.commit()


# to get all data from db 
users = new_session.query(Users)

# then use for on users

# order by
users = new_session.query(Users).order_by(Users.name)
# where
users = new_session.query(Users).filter(Users.name=="qaiser 1")
# get first
users = new_session.query(Users).first()


# update record
first_user = new_session.query(Users).first()
first_user.name = "qaiser"
new_session.commit()

# delete record
first_user = new_session.query(Users).first()
new_session.delete(first_user)
new_session.commit()