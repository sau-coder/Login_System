from databases.database import base
from sqlalchemy import String , Integer , Column
from sqlalchemy import UniqueConstraint


class UserSignup(base):
    __tablename__ = "user_login_data"
    first_name = Column(String)
    last_name = Column(String)
    user_name = Column(String , primary_key = True)
    email_id = Column(String , unique = True)
    mobile_no = Column(Integer , unique = True)
    password = Column(String)
    retype_password = Column(String)


