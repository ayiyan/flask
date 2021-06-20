from apiframework.models.dbobject.users_table import Users
from apiframework.models.db_connection import Session

class UserMgr(object):
    @staticmethod
    def save(*args, **kwargs):
        db_session = Session()
        user_obj = Users(id=125, name='alex3')
        db_session.add(user_obj)
        db_session.commit()
        db_session.close()

    @staticmethod
    def select_all(*args,**kwargs):
        db_session = Session()
        res = db_session.query(Users).all()
        db_session.close()
        return res
        
